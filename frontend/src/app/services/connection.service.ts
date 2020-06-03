import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { map, catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ConnectionService {
  public type: string;
  public baseUrl: string;
  constructor(private http: HttpClient) {
    this.type = null;
    this.baseUrl = 'http://127.0.0.1:5000/';
    this.proof();
  }
  private handleError(error: HttpErrorResponse) {
    console.log(error);
    return throwError('Error! something went wrong. >:v');
  }

  proof() {
     this.http.get(this.baseUrl).subscribe(data => {
            console.log(data);
    });
  }
}
