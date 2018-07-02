import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatToolbarModule} from '@angular/material/toolbar';

@NgModule({
  imports: [
    MatToolbarModule
  ],
  exports: [
    MatToolbarModule
  ],
})
export class MaterialModule { }