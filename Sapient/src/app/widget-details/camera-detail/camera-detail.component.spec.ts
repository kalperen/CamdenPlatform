import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing'; 
import { ClassificationService }  from '../../classification.service';
import { CameraDetailComponent } from './camera-detail.component';

describe('CameraDetailComponent', () => {
  let component: CameraDetailComponent;
  let fixture: ComponentFixture<CameraDetailComponent>;
  let classificationService = ClassificationService;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ 
        FormsModule,
        MatToolbarModule,
        MatTableModule,
        HttpClientModule,
        HttpClientTestingModule,
        RouterTestingModule.withRoutes(
          [{path: 'Kinect', component: CameraDetailComponent}]
        )
      ],
      declarations: [ CameraDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CameraDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
