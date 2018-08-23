import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing'; 
import { TemperatureWidgetDetailComponent } from './temperature-widget-detail.component';
import { WidgetService }  from '../../widget.service';
import { TelemetryService }  from '../../telemetry.service';

describe('TemperatureWidgetDetailComponent', () => {
  let component: TemperatureWidgetDetailComponent;
  let fixture: ComponentFixture<TemperatureWidgetDetailComponent>;
  let widgetService = WidgetService;
  let telemetryService = TelemetryService;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ 
        FormsModule,
        MatToolbarModule,
        MatTableModule,
        HttpClientModule,
        HttpClientTestingModule,
        RouterTestingModule.withRoutes(
          [{path: 'temperature', component: TemperatureWidgetDetailComponent}]
        )
      ],
      declarations: [ TemperatureWidgetDetailComponent ],
      providers: [
        { provide: WidgetService, useClass: WidgetService },
        { provide: TelemetryService, useClass: TelemetryService }
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TemperatureWidgetDetailComponent);
    component = fixture.componentInstance;
    widgetService = TestBed.get(WidgetService);
    telemetryService = TestBed.get(TelemetryService);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('widget should be unefined before creation', () =>{
    expect(component.widget).toBeUndefined();
  });

  // it('widget not to be undefined after creation', () =>{
  //   component.ngOnInit();
  //   expect(component.widget).not.toBeUndefined();
  // });
});
