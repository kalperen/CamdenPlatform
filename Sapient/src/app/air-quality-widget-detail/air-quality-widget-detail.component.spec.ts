import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AirQualityWidgetDetailComponent } from './air-quality-widget-detail.component';

describe('AirQualityWidgetDetailComponent', () => {
  let component: AirQualityWidgetDetailComponent;
  let fixture: ComponentFixture<AirQualityWidgetDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
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
