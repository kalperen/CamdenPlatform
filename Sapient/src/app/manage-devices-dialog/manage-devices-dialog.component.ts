import { Component, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

import { AddDeleteDeviceComponent } from '../add-delete-device/add-delete-device.component';

@Component({
  selector: 'app-manage-devices-dialog',
  templateUrl: './manage-devices-dialog.component.html',
  styleUrls: ['./manage-devices-dialog.component.css']
})
export class ManageDevicesDialogComponent implements OnInit {

  constructor(
    public dialog: MatDialog
  ) { }

  ngOnInit() {
  }

  openDialog(operation, device): void {
    const dialogRef = this.dialog.open(AddDeleteDeviceComponent, {
      data: { 
        operation: operation,
        device: device
      },
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

}
