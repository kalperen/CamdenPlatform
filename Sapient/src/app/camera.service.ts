import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

import { Camera } from './camera';

@Injectable({
  providedIn: 'root'
})
export class CameraService {
  public serverUrl = 'https://sapient-server.azurewebsites.net/cameras/getCameras';
  
  constructor(private http: HttpClient) { }

  getCameras(): Observable<Camera[]> {
    return this.http.get<Camera[]>(this.serverUrl)
    .pipe(
      tap(() => console.log(`fetched cameras`)),
      catchError(this.handleError('getCameras', []))
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
