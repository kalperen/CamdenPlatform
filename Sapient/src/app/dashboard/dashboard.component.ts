import { Component, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

import { WidgetService } from '../widget.service';
import { Widget } from '../widget';
import { CameraService } from '../camera.service';
import { Camera } from '../camera';
import { ManageDevicesDialogComponent } from '../manage-devices-dialog/manage-devices-dialog.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements OnInit {
  
  widgets: Widget[];
  cameras: Camera[];
  private deviceId;

  constructor(
    public widgetService: WidgetService,
    public cameraService: CameraService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {
    this.getWidgets();
    this.getCameras();
  }

  getWidgets(): void {
    this.widgetService.getWidgets()
      .subscribe(widgets => this.widgets = widgets);
  }

  getCameras(): void {
    this.cameraService.getCameras()
      .subscribe(cameras => this.cameras = cameras);
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
