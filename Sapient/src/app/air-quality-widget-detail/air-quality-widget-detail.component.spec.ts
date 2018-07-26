import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
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
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
