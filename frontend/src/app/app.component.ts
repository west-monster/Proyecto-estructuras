import { Component, OnInit } from '@angular/core';
import { UndoNoUndoService } from './services/undo-no-undo.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent  {
  public showF: boolean;
  constructor(public history: UndoNoUndoService){
    this.showF = false;

  }
  show(){
    this.showF = !this.showF;
  }
}
