import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

import { WidgetService } from '../widget.service';
import { Widget } from '../widget';
import { ManageDevicesDialogComponent } from '../manage-devices-dialog/manage-devices-dialog.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})



export class DashboardComponent implements OnInit {
  
  widgets: Widget[];
  private serverUrl = "http://localhost:3000/devices/addDevice";
  private deviceId;
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor(
    public widgetService: WidgetService,
    private http: HttpClient,
    public dialog: MatDialog
  ) { }

  getWidgets(): void {
    this.widgetService.getWidgets()
      .subscribe(widgets => this.widgets = widgets);
  }

  ngOnInit() {
    this.getWidgets();
  }

  addDevice(): void{
    this.deviceId = "test-device-" + (1000) * Math.random();
    this.http.post(this.serverUrl, { deviceId: this.deviceId }, this.httpOptions)
    .subscribe(
      res => {
        console.log(res);
      },
      err => {
        console.log("Error occured: " + err);
      }
    );
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(ManageDevicesDialogComponent, {
      width: '250px',
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

}
