import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { WidgetService }  from '../widget.service';
import { Widget } from '../widget'

@Component({
  selector: 'app-widget',
  templateUrl: './widget.component.html',
  styleUrls: ['./widget.component.css']
})

export class WidgetComponent implements OnInit {
  @Input() widget: Widget;

  constructor(
    private route: ActivatedRoute,
    private widgetService: WidgetService,
    private location: Location) {}

  ngOnInit() {
    this.getWidget();
  }

  getWidget(): void {
    const sensorId = this.route.snapshot.paramMap.get('sensorId');
    this.widgetService.getWidget(sensorId)
      .subscribe(widget => this.widget = widget);
  }

  goBack(): void {
    this.location.back();
  }
}
