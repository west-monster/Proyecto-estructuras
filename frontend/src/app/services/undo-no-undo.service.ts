import { Injectable } from '@angular/core';
import { Queue } from './Structures/Queue';
import { TypeAction, History } from '../Interfaces/intefaces';
import { ConnectionService } from './connection.service';
import { Stack } from './Structures/Stack';
@Injectable({
  providedIn: 'root'
})
export class UndoNoUndoService {
  public back: Queue;
  public adv: Stack;
  public history: History[];
  constructor(private conn: ConnectionService) {
    this.adv = new Stack();
    this.back = new Queue();
    this.history = [];
  }
  addAction(type: TypeAction){
    if (this.history.length === 10) {
      this.back.dequeue();
    }
    this.setHistory(type);
    this.back.enqueue(type);
    this.adv = new Stack();
    console.log(this.back);
  }
  setHistory(type: TypeAction) {
    if (this.history.length === 10 ) {
      this.history.pop();
    }
    this.history.push({
      type: type.type,
      nombre: type.new.length > 0 ? type.new[0].nombre : ''
    });
  }
  undo(){
    if (!this.back.empty()) {
      const aux: TypeAction = this.back.pop();
      console.log(aux);
      this.setHistory(aux);
      switch (aux.type) {
        case 0:
          this.conn.edit(aux.past[0]).subscribe((ans: boolean) => {
            this.adv.push({
              type: 0,
              new: aux.past,
              past: aux.new
            });
          });
          break;
        case 1:
          this.conn.add(aux.new[0]).subscribe((ans: boolean) => {
            this.adv.push({
              type: -1,
              new: aux.past,
              past: aux.new
            });
          });
          break;
        default:
          console.error('Not valid');
      }
    }
  }
  noUndo(){
    if (!this.adv.empty()) {
      const aux: TypeAction = this.adv.pop();
      console.log(aux);
      this.setHistory(aux);
      switch (aux.type) {
        case 0:
          this.conn.edit(aux.past[0]).subscribe((ans: boolean) => {
          this.back.enqueue({
            type: 0,
            new: aux.past,
            past: aux.new
          });
          });
          break;
          case -1:
            const auxNames: string[] = [];
            aux.past.forEach(element => {
              auxNames.push(element.nombre);
            });
            this.conn.delete(auxNames).subscribe((ans: boolean) => {
              this.back.enqueue({
                type: 1,
                new: aux.past,
                past: aux.new
              });
            });
            break;
        default:
          console.error('Not valid');
      }
  }
  }
}
