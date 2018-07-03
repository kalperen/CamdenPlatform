import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent }   from './dashboard/dashboard.component';
import { WidgetComponent } from './widget/widget.component';
import { TemperatureWidgetDetailComponent } from './temperature-widget-detail/temperature-widget-detail.component';
import { AirQualityWidgetDetailComponent } from './air-quality-widget-detail/air-quality-widget-detail.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'detail/temperature/:sensorId', component: TemperatureWidgetDetailComponent },
  { path: 'detail/air/:sensorId', component: AirQualityWidgetDetailComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [ RouterModule ],
  declarations: []
})
export class AppRoutingModule { } 
