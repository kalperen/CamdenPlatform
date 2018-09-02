import { Component, OnInit, Inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { ManageDevicesDialogComponent } from '../manage-devices-dialog/manage-devices-dialog.component';



@Component({
  selector: 'app-add-delete-device',
  templateUrl: './add-delete-device.component.html',
  styleUrls: ['./add-delete-device.component.css']
})
export class AddDeleteDeviceComponent implements OnInit {
  private result = null;
  public serverUrl = "https://sapient-server.azurewebsites.net/";
  private deviceId: string;
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor(
    @Inject(MAT_DIALOG_DATA) public data: any,
    private http: HttpClient,
    private dialogRef: MatDialogRef<ManageDevicesDialogComponent>
  ) { }

  ngOnInit() {
  }

  makeOperation() : void{
    if (this.data.operation == 'Add')
      this.addDevice();
    else
      this.deleteDevice();
  }

  addDevice(): void{
    let endpoint = (this.data.device == 'Device') ? 'devices/addDevice' : 'cameras/addCamera';
    let data = {};
    if (this.data.device == 'Device'){
      data = { deviceId: this.deviceId };
    } else {
      data = { cameraId: this.deviceId };
    }
    this.http.post(this.serverUrl + endpoint, data, this.httpOptions)
    .subscribe(
      res => {
        if (this.data.device == 'Device')
          this.result = res;
        console.log(res);
      },
      err => {
        console.log("Error occured: " + err);
      }
    );
  }
  
  deleteDevice(): void{
    let endpoint = ((this.data.device == 'Device') ? 'devices/device/' : 'cameras/deleteCamera/') + this.deviceId;
    this.http.delete(this.serverUrl + endpoint)
    .subscribe(
      res => {
        console.log(res);
      },
      err => {
        console.log("Error occured: " + err);
      }
    );
  }
}
