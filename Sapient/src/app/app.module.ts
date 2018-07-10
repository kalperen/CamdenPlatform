import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { MaterialModule } from './material.module';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './/app-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { WidgetComponent } from './widget/widget.component';
import { TemperatureWidgetDetailComponent } from './temperature-widget-detail/temperature-widget-detail.component';
import { AirQualityWidgetDetailComponent } from './air-quality-widget-detail/air-quality-widget-detail.component';
import { ManageDevicesDialogComponent } from './manage-devices-dialog/manage-devices-dialog.component';
import { AddDeleteDeviceComponent } from './add-delete-device/add-delete-device.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    WidgetComponent,
    TemperatureWidgetDetailComponent,
    AirQualityWidgetDetailComponent,
    ManageDevicesDialogComponent,
    AddDeleteDeviceComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [
    ManageDevicesDialogComponent,
    AddDeleteDeviceComponent
  ]
})
export class AppModule { }
