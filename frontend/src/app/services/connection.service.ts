import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { throwError, Observable } from 'rxjs';
import elms from './data.json';
import { DataTable, QueryData } from '../Interfaces/intefaces';

@Injectable({
  providedIn: 'root'
})
export class ConnectionService {
  public type: string;
  public baseUrl: string;
  constructor(private http: HttpClient) {
    this.type = null;
    this.baseUrl = 'http://127.0.0.1:5000/';
  }
  private handleError(error: HttpErrorResponse) {
    console.log(error);
    return throwError('Error! something went wrong. >:v');
  }
  sort(target: string): Observable<QueryData>{
    let aux = {
      data: [],
      totalResults: 0
    };
    aux.data = elms;
    aux.totalResults = elms.length;
    let aux2 = new Observable<QueryData>((observer) => {

      // Simple geolocation API check provides values to publish
      observer.next(aux);

      // When the consumer unsubscribes, clean up data ready for next subscription.
      return {
        unsubscribe() {
        }
      };
    });
    return aux2;
  }

  setArrows(target: string, limit: number): Observable<QueryData>{
    let aux = {
      data: [],
      totalResults: 0
    };
    aux.data = elms;
    aux.totalResults = elms.length;
    let aux2 = new Observable<QueryData>((observer) => {

      // Simple geolocation API check provides values to publish
      observer.next(aux);

      // When the consumer unsubscribes, clean up data ready for next subscription.
      return {
        unsubscribe() {
        }
      };
    });
    return aux2;
  }
  setPage(target: string, first: number, limit: number): Observable<QueryData>{
    console.log('Select * From table WHERE id > ' + first + ' limit ' + limit);
    let aux = {
      data: [],
      totalResults: 0
    };
    aux.data = elms.slice(first, first + limit);
    aux.totalResults = elms.length;
    let aux2 = new Observable<QueryData>((observer) => {

      // Simple geolocation API check provides values to publish
      observer.next(aux);

      // When the consumer unsubscribes, clean up data ready for next subscription.
      return {
        unsubscribe() {
        }
      };
    });
    return aux2;
  }
}
