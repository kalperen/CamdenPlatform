import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageDevicesDialogComponent } from './manage-devices-dialog.component';

describe('ManageDevicesDialogComponent', () => {
  let component: ManageDevicesDialogComponent;
  let fixture: ComponentFixture<ManageDevicesDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManageDevicesDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManageDevicesDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
