import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { MatDialogModule, MatInputModule, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AddDeleteDeviceComponent } from './add-delete-device.component';

describe('AddDeleteDeviceComponent', () => {
  let component: AddDeleteDeviceComponent;
  let fixture: ComponentFixture<AddDeleteDeviceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ 
        FormsModule,
        MatDialogModule,
        MatInputModule,
        HttpClientModule,
        HttpClientTestingModule,
        BrowserAnimationsModule
      ],
      providers: [
        { provide: MAT_DIALOG_DATA, useValue: {
          operation : "Add",
          device : "Device"
          } 
        },
        { provide : MatDialogRef, useValue : {} }
      ],
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

  it('should add device', () => {
    component.serverUrl = "test url";
    component.makeOperation();
    expect(component).toBeTruthy();
  });

  it('should add camera', () => {
    component.serverUrl = "test url";
    component.data.device = "Camera";
    component.makeOperation();
    expect(component).toBeTruthy();
  });

  it('should delete', () => {
    component.serverUrl = "test url";
    component.data.operation = "Delete";
    component.makeOperation();
    expect(component).toBeTruthy();
  });
});
