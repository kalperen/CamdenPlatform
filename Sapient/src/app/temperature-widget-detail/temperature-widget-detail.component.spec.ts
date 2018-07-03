import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TemperatureWidgetDetailComponent } from './temperature-widget-detail.component';

describe('TemperatureWidgetDetailComponent', () => {
  let component: TemperatureWidgetDetailComponent;
  let fixture: ComponentFixture<TemperatureWidgetDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TemperatureWidgetDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TemperatureWidgetDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
