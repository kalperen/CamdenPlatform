import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ClassificationService }  from '../../classification.service';
import { Classification } from '../../classification';

@Component({
  selector: 'app-camera-detail',
  templateUrl: './camera-detail.component.html',
  styleUrls: ['./camera-detail.component.css']
})
export class CameraDetailComponent implements OnInit {
  classifications: Classification[];
  cameraId: string;
  displayedColumns: string[] = ['time', 'sitting', 'standing', 'laying'];

  constructor(
    private route: ActivatedRoute,
    private ClassificationService: ClassificationService
  ) { }

  ngOnInit() {
    this.getClassifications();
  }

  getClassifications(): void {
    this.cameraId = this.route.snapshot.paramMap.get('cameraId');

    const classificationQuery = {
      cameraId : this.cameraId
    }

    this.ClassificationService.getClassifications(classificationQuery)
      .subscribe(classifications => {this.classifications = classifications;});
  }

}
