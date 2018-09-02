import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { Telemetry } from './telemetry';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})

export class TelemetryService {
  public serverUrl = "https://sapient-server.azurewebsites.net/telemetries/getTelemetries";

  constructor(private http: HttpClient) { }

  getTelemetries(telemetryQuery : Object) : Observable<Telemetry[]>{

    //remove null fields from object
    Object.keys(telemetryQuery).forEach((key) => (telemetryQuery[key] == null) && delete telemetryQuery[key]);

    return this.http.post<Telemetry[]>(this.serverUrl, telemetryQuery, httpOptions).pipe(
      tap((telemetries: Telemetry[]) => console.log(telemetries)),
      catchError(this.handleError<Telemetry[]>('getTelemetries'))
    );
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
 
      console.log(`${operation} failed: ${error.message}`);
 
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
