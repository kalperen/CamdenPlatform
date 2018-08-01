import { Component, OnInit, Input, ElementRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { ClassificationService }  from '../classification.service';
import { Classification } from '../classification';

import { Camera } from '../camera'

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.css']
})

export class CameraComponent implements OnInit {
  @Input() camera: Camera;
  @Input() cameraId: string;
  classifications: Classification[];
  avg: number;

  constructor(
    private route: ActivatedRoute,
    private classificationService: ClassificationService,
    private elm: ElementRef
  ) { }

  ngOnInit() {
    this.getClassifications();
  }

  getClassifications(): void{
    const classificationQuery = {
      cameraId : this.cameraId
    }

    this.classificationService.getClassifications(classificationQuery)
      .subscribe(classifications => {
        var count = 0;
        var total = 0;
        for (let c of classifications){
          let sum = Number(c.sitting) + Number(c.standing) + Number(c.laying);
          console.log("sum " + sum);
          count++;
          total += sum;
        }
        
        this.avg = total/count;
        this.classifications = classifications;
      });
  }
}
