import { Component, OnInit, Input, ElementRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { WidgetService }  from '../widget.service';
import { Widget } from '../widget'
import { TelemetryService }  from '../telemetry.service';
import { Telemetry } from '../telemetry';

@Component({
  selector: 'app-widget',
  templateUrl: './widget.component.html',
  styleUrls: ['./widget.component.css']
})

export class WidgetComponent implements OnInit {
  @Input() widget: Widget;
  @Input() sensorId: string;
  telemetries: Telemetry[];
  avg: number;

  constructor(
    private route: ActivatedRoute,
    private widgetService: WidgetService,
    private telemetryService: TelemetryService,
    private elm: ElementRef) {}

  ngOnInit() {
    this.getWidget();
  }

  getWidget(): void {
    this.widgetService.getWidget(this.sensorId)
      .subscribe(widget => {this.widget = widget; this.getTelemetries();});
  }

  getTelemetries(): void{
    const telemetryQuery = {
      sensorType : this.widget.sensorType
    }

    this.telemetryService.getTelemetries(telemetryQuery)
      .subscribe(telemetries => {
        var count = 0;
        var total = 0;
        for (let t of telemetries){
          count++;
          total += t.measurementValue;
        }
        this.avg = total/count;
        console.log("avg " + this.avg);
        this.telemetries = telemetries;
      });
  }
}
