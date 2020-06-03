import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EditService {

  private triggerEdit = new Subject<number>();
  public triggerEdit$: Observable<number>;
  constructor() {
    this.triggerEdit$ = this.triggerEdit.asObservable();
  }
  snedId(id: number) {
    this.triggerEdit.next(id);
  }
}
