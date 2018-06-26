import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { WidgetService } from '../widget.service';
import { Widget } from '../widget';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})



export class DashboardComponent implements OnInit {
  
  widgets: Widget[];
  private serverUrl = "http://localhost:3000/addDevice";
  private deviceId;
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };
  constructor(
    public widgetService: WidgetService,
    private http: HttpClient
  ) { }

  getWidgets(): void {
    this.widgetService.getWidgets()
      .subscribe(heroes => this.widgets = heroes);
  }

  ngOnInit() {
    this.getWidgets();
  }

  addDevice(): void{
    this.deviceId = "test-device-" + (1000) * Math.random();
    console.log(this.deviceId);
    this.http.post(this.serverUrl, { deviceId: this.deviceId }, this.httpOptions)
    .subscribe(
      res => {
        console.log(res);
      },
      err => {
        console.log("Error occured: " + err);
      }
    );;
  }

}
