import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { WidgetService }  from '../widget.service';
import { Widget } from '../widget'
import { TelemetryService }  from '../telemetry.service';
import { Telemetry } from '../telemetry';

@Component({
  selector: 'app-air-quality-widget-detail',
  templateUrl: './air-quality-widget-detail.component.html',
  styleUrls: ['./air-quality-widget-detail.component.css']
})
export class AirQualityWidgetDetailComponent implements OnInit {
  @Input() widget: Widget;
  telemetries: Telemetry[];

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
      .subscribe(telemetries => this.telemetries = telemetries);
  }

  goBack(): void {
    this.location.back();
  }
}