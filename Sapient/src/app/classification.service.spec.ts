import { TestBed, inject } from '@angular/core/testing';
import { HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ClassificationService } from './classification.service';

describe('ClassificationService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ 
        HttpClientModule,
        HttpClientTestingModule
      ],
      providers: [ClassificationService]
    });
  });

  it('should be created', inject([ClassificationService], (service: ClassificationService) => {
    expect(service).toBeTruthy();
  }));

  it('should get non empty result', inject([ClassificationService], (service: ClassificationService) => { 
    service.getClassifications({}) 
      .subscribe(classifications => expect(classifications.length).toBeGreaterThan(0)); 
  })); 

  it('should return empty if error', inject([ClassificationService], (service: ClassificationService) => { 
    service.serverUrl = "invalid url";
    service.getClassifications({}) 
      .subscribe(widgets => expect(widgets.length).toBe(0)); 
  })); 
});
