import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { MatDialogModule, MatInputModule, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material';
import { ManageDevicesDialogComponent } from './manage-devices-dialog.component';

describe('ManageDevicesDialogComponent', () => {
  let component: ManageDevicesDialogComponent;
  let fixture: ComponentFixture<ManageDevicesDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ 
        FormsModule,
        MatDialogModule,
        MatInputModule
      ],
      providers: [
        { provide: MAT_DIALOG_DATA, useValue: {} },
        { provide : MatDialogRef, useValue : {} }
      ],
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
