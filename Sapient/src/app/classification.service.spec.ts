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
});
