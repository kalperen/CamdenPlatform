import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { Widget } from './widget';
import { WIDGETS } from './mock-widgets';

@Injectable({
  providedIn: 'root'
})
export class WidgetService {

  constructor() { }

  getWidgets(): Observable<Widget[]> {
    // TODO: send the message _after_ fetching the heroes
    return of(WIDGETS);
  }

  getWidget(sensorId: string): Observable<Widget> {
    // TODO: send the message _after_ fetching the hero
    return of(WIDGETS.find(widget => widget.sensorId === sensorId));
  }
}
