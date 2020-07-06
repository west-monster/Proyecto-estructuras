import { Component, OnInit, Input, ViewChild, AfterViewInit, OnDestroy } from '@angular/core';
import { DataTable } from '../../Interfaces/intefaces';
import { SearchComponent } from '../../shared/search/search/search.component';
import { ConnectionService } from '../../services/connection.service';
import { UndoNoUndoService } from '../../services/undo-no-undo.service';
import { AddComponent } from '../../shared/add/add.component';
import { formatDate } from '@angular/common';
import { EditService } from '../../edit/edit/edit.service';
import { Subscription } from 'rxjs';
import { FormGroup, FormControl, Validators } from '@angular/forms';
declare var $: any;

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements AfterViewInit, OnDestroy {

  @ViewChild(SearchComponent) searcher;
  @ViewChild(AddComponent) adder;
  private subscription: Subscription;
  protected idEdit: number;
  protected childLoad: boolean;
  public sold: FormGroup;
  constructor(protected conn: ConnectionService, public history: UndoNoUndoService, public shareAux: EditService){
    this.childLoad = false;
    this.idEdit = null;
    this.subscription = this.shareAux.triggerEdit$.subscribe(
      id => {
        console.log(id);
        this.load(id);
    });
    this.sold = new FormGroup({
      tar: new FormControl('', [Validators.pattern('^[0-9.,]*$'), Validators.required, this.top.bind(this)])
    });
  }
  top(control: FormControl){
    return (this.childLoad && control.value > this.searcher.table.data[this.idEdit].cantidad) ? { big: true } :  null  ;
  }
  delete(){
    let aux: string[] = [];
    const historyAction: DataTable[] = [];
    this.searcher.sendSelected().forEach(id => {
      aux.push(this.searcher.table.data[id].nombre);
      historyAction.push(this.searcher.table.data[id]);
    });
    this.conn.delete(aux).subscribe((ans: boolean) => {
      ans ? console.log(1) : console.log(0);
      this.searcher.submit();
      this.history.addAction({
        type: 1,
        new: historyAction,
        past: historyAction
      });
      this.searcher.table.selecterSaver = [];
    });
  }
  deleteAllModal(){
    $('#modalDeleteAll').modal();
  }
  get data(){
    return this.childLoad ?  this.searcher.table.selecterSaver.length : 0;
  }
  deleteAll(){
    this.conn.deleteAll().subscribe((ans: boolean) => {
      $('#modalDeleteAll').modal('hide');
    });

  }

  ngAfterViewInit(): void {
    this.childLoad = true;
    this.adder.edit.get('nombre').disable();
  }

  load(id: number){
    this.adder.edit.reset(this.searcher.table.data[id]);
    const date: Date = new Date(this.searcher.table.data[id].fecha);
    this.adder.edit.get('fecha').setValue(formatDate(date, 'yyyy-MM-dd', 'en'));
    this.idEdit = id;
  }
  submit(){
    this.adder.edit.get('nombre').enable();
    const aux = this.adder.edit.value;
    aux.id = this.searcher.table.data[this.idEdit].id;
    console.log(aux);
    this.conn.edit(aux).subscribe((ans: boolean) => {
      this.searcher.submit();
      this.adder.edit.get('nombre').disable();
      this.history.addAction({
        type: 0,
        past: [this.searcher.table.data[this.idEdit]],
        new: [aux]
      });
      $('#modalAdd').modal('hide');
    });
  }

  sell(){
    console.log(this.searcher.table.data[this.idEdit]);
    const aux = this.searcher.table.data[this.idEdit];
    aux.cantidad  = this.searcher.table.data[this.idEdit].cantidad - this.sold.get('tar').value;

    console.log(aux);
    this.conn.edit(aux).subscribe((ans: boolean) => {
      this.searcher.submit();
      this.history.addAction({
        type: 0,
        past: [this.searcher.table.data[this.idEdit]],
        new: [aux]
      });
      $('#sellModal').modal('hide');
      this.sold.get('tar').setValue('');
    });
  }

  get valid(){
    return this.childLoad ? this.adder.edit.valid : false;
  }
  get amount() {
    return this.idEdit != null ? this.searcher.table.data[this.idEdit].cantidad : 0;
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }


}
