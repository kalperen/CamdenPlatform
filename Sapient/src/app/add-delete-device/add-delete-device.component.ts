import { Component, OnInit, Inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {MAT_DIALOG_DATA} from '@angular/material';

@Component({
  selector: 'app-add-delete-device',
  templateUrl: './add-delete-device.component.html',
  styleUrls: ['./add-delete-device.component.css']
})
export class AddDeleteDeviceComponent implements OnInit {

  private serverUrl = "http://localhost:3000/";
  private deviceId: string;
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };

  constructor(
    @Inject(MAT_DIALOG_DATA) public data: any,
    private http: HttpClient
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
    this.http.post(this.serverUrl + endpoint, { deviceId: this.deviceId }, this.httpOptions)
    .subscribe(
      res => {
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
