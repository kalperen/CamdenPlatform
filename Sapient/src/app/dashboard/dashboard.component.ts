import { Component, OnInit } from '@angular/core';
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
  private deviceId;

  constructor(
    public widgetService: WidgetService,
    public dialog: MatDialog
  ) { }

  getWidgets(): void {
    this.widgetService.getWidgets()
      .subscribe(widgets => this.widgets = widgets);
  }

  ngOnInit() {
    this.getWidgets();
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
