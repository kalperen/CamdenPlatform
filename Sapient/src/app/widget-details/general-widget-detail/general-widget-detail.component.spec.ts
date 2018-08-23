import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GeneralWidgetDetailComponent } from './general-widget-detail.component';

import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing'; 
import { WidgetService }  from '../../widget.service';
import { TelemetryService }  from '../../telemetry.service';

describe('GeneralWidgetDetailComponent', () => {
  let component: GeneralWidgetDetailComponent;
  let fixture: ComponentFixture<GeneralWidgetDetailComponent>;
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
          [{path: 'temperature', component: GeneralWidgetDetailComponent}]
        )
      ],
      declarations: [ GeneralWidgetDetailComponent ],
      providers: [
        { provide: WidgetService, useClass: WidgetService },
        { provide: TelemetryService, useClass: TelemetryService }
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GeneralWidgetDetailComponent);
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
});
