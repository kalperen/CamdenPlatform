import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddDeleteDeviceComponent } from './add-delete-device.component';

describe('AddDeleteDeviceComponent', () => {
  let component: AddDeleteDeviceComponent;
  let fixture: ComponentFixture<AddDeleteDeviceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddDeleteDeviceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddDeleteDeviceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
