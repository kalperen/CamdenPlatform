import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent }   from './dashboard/dashboard.component';
import { CameraDetailComponent } from './widget-details/camera-detail/camera-detail.component';
import { TemperatureWidgetDetailComponent } from './widget-details/temperature-widget-detail/temperature-widget-detail.component';
import { AirQualityWidgetDetailComponent } from './widget-details/air-quality-widget-detail/air-quality-widget-detail.component';
import { GeneralWidgetDetailComponent } from './widget-details/general-widget-detail/general-widget-detail.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'detail/temperature/:sensorId', component: TemperatureWidgetDetailComponent },
  { path: 'detail/air/:sensorId', component: AirQualityWidgetDetailComponent },
  { path: 'detail/light/:sensorId', component: GeneralWidgetDetailComponent },
  { path: 'detail/camera/:cameraId', component: CameraDetailComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [ RouterModule ],
  declarations: []
})
export class AppRoutingModule { } 
