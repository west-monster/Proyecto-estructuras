import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { throwError, Observable } from 'rxjs';
import elms from './data.json';
import { map, catchError } from 'rxjs/operators';
import { DataTable } from '../Interfaces/intefaces';

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
  seeAll(first: number, last: number){
    return this.http.get(this.baseUrl + `seeAll?first=${first}&last=${last}`)
    .pipe( catchError(this.handleError));
  }

  search(target: string){
    return this.http.get(this.baseUrl + `search?target=${target}`)
    .pipe( catchError(this.handleError));
  }
  delete(targets: number[]){
    return this.http.post(this.baseUrl + 'delete', { targets})
    .pipe( catchError(this.handleError));
  }
  deleteAll(){
    return this.http.delete(this.baseUrl + 'deleteAll')
    .pipe( catchError(this.handleError));
  }
  edit(target: any){
    return this.http.post(this.baseUrl + 'edit', target)
    .pipe( catchError(this.handleError));
  }
}
