import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import Plotly from 'plotly.js-dist';

import { WidgetService }  from '../../widget.service';
import { Widget } from '../../widget'
import { TelemetryService }  from '../../telemetry.service';
import { Telemetry } from '../../telemetry';

@Component({
  selector: 'app-air-quality-widget-detail',
  templateUrl: './air-quality-widget-detail.component.html',
  styleUrls: ['./air-quality-widget-detail.component.css']
})
export class AirQualityWidgetDetailComponent implements OnInit {
  @Input() widget: Widget;
  telemetries: Telemetry[];
  displayedColumns: string[] = ['sensorType', 'deviceId', 'measurementValue', 'measurementUnit'];

  constructor(
    private route: ActivatedRoute,
    private widgetService: WidgetService,
    private telemetryService: TelemetryService,
    private location: Location) { }

  ngOnInit() {
    this.getWidget();
  }

  getWidget(): void {
    const sensorId = this.route.snapshot.paramMap.get('sensorId');
    this.widgetService.getWidget(sensorId)
      .subscribe(widget => {this.widget = widget; this.getTelemetries();});
  }

  getTelemetries(): void{
    const telemetryQuery = {
      sensorType : this.widget.sensorType
    }

    this.telemetryService.getTelemetries(telemetryQuery)
      .subscribe(telemetries => {
        this.telemetries = telemetries;
        this.printGraph();
      });
  }

  printGraph(): void{
    var sensors = {};

    for (let telemetry of this.telemetries){
      if(!sensors[String(telemetry.deviceId)]){
        sensors[String(telemetry.deviceId)] = {
          measurements: [],
          times: []
        };
      }

      sensors[String(telemetry.deviceId)].measurements.push(telemetry.measurementValue);
      let time = telemetry.year + "-" + telemetry.month + "-" + telemetry.day + " " + (telemetry.hour < 10 ? "0" : "") + telemetry.hour + ":"+  (telemetry.minutes < 10 ? "0" : "") + telemetry.minutes + ":00.000000";
      sensors[String(telemetry.deviceId)].times.push(time);
    }

    console.log(sensors);

    var data = [];

    for (let sensor in sensors){
      let v = {
        y: sensors[sensor].measurements,
        x: sensors[sensor].times,
        name: sensor
      }
      data.push(v);
    }

    Plotly.newPlot('graph', data);

  }
}