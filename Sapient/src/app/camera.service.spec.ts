import { TestBed, inject } from '@angular/core/testing';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CameraService } from './camera.service';

describe('CameraService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ 
        HttpClientModule,
        HttpClientTestingModule
      ],
      providers: [CameraService]
    });
  });

  it('should be created', inject([CameraService], (service: CameraService) => {
    expect(service).toBeTruthy();
  }));

  it('should get non empty result', inject([CameraService], (service: CameraService) => {
    service.getCameras()
      .subscribe(cameras => expect(cameras.length).toBeGreaterThan(0));
  }));

  it('should return empty if error', inject([CameraService], (service: CameraService) => { 
    service.serverUrl = "invalid url";
    service.getCameras() 
      .subscribe(widgets => expect(widgets.length).toBe(0)); 
  })); 
});
