import { TestBed, inject } from '@angular/core/testing';

import { ClassificationService } from './classification.service';

describe('ClassificationService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ClassificationService]
    });
  });

  it('should be created', inject([ClassificationService], (service: ClassificationService) => {
    expect(service).toBeTruthy();
  }));
});
