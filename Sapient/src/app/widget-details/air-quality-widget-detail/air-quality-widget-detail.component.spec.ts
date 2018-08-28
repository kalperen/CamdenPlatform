import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { AirQualityWidgetDetailComponent } from './air-quality-widget-detail.component';
import { RouterTestingModule } from '@angular/router/testing'; 

describe('AirQualityWidgetDetailComponent', () => {
  let component: AirQualityWidgetDetailComponent;
  let fixture: ComponentFixture<AirQualityWidgetDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ 
        FormsModule,
        MatToolbarModule,
        MatTableModule,
        HttpClientModule,
        HttpClientTestingModule,
        RouterTestingModule.withRoutes(
          [{path: 'air', component: AirQualityWidgetDetailComponent}]
        )
      ],
      declarations: [ AirQualityWidgetDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AirQualityWidgetDetailComponent);
    component = fixture.componentInstance;
    component.widget = {
      sensorType: 'air-quality',
      sensorId: '1',
      telemetries: []
    };
    component.telemetries = [{
      sensorType: 'air-quality',
      deviceId: '1',
      measurementUnit: 'C',
      measurementValue: 23,
      hour: 12,
      minutes: 12,
      seconds: 12,
      year: 2018,
      month: 3,
      day: 26
    }];
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('get telemetries', () =>{
    component.getTelemetries();
  });

  // it('get plot', () =>{
  //   component.printGraph();
  // });
});
