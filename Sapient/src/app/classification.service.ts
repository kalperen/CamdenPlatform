import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { Classification } from './classification';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})

export class ClassificationService {
  public serverUrl = "https://sapient-server.azurewebsites.net/classifications/getClassifications";

  constructor(private http: HttpClient) { }

  getClassifications(classificationQuery : Object) : Observable<Classification[]>{

    //remove null fields from object
    Object.keys(classificationQuery).forEach((key) => (classificationQuery[key] == null) && delete classificationQuery[key]);

    return this.http.post<Classification[]>(this.serverUrl, classificationQuery, httpOptions).pipe(
      tap((classifications: Classification[]) => console.log(classifications)),
      catchError(this.handleError<Classification[]>('getClassifications'))
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
