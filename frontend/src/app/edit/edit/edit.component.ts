import { Component, OnInit, ViewChild, OnDestroy, AfterViewInit } from '@angular/core';
import { SearchComponent } from '../../shared/search/search/search.component';
import { DataTable } from '../../Interfaces/intefaces';
import { EditService } from './edit.service';
import { Subscription } from 'rxjs';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { formatDate } from '@angular/common';
import { AddComponent } from '../../shared/add/add.component';
import { ConnectionService } from '../../services/connection.service';
import { UndoNoUndoService } from '../../services/undo-no-undo.service';
declare var $: any;
@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnDestroy, AfterViewInit {


  @ViewChild(SearchComponent) searcher;
  @ViewChild(AddComponent) adder;
  private subscription: Subscription;
  private idEdit: number;
  private loadChild: boolean;
  constructor(public shareAux: EditService, private conn: ConnectionService, public history: UndoNoUndoService) {
    this.idEdit = null;
    this.loadChild = false;
    this.subscription = this.shareAux.triggerEdit$.subscribe(
      id => {
        console.log(id);
        this.load(id);
    });
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

  get valid(){
    return this.loadChild ? this.adder.edit.valid : false;
  }

  ngAfterViewInit(){
    this.loadChild = true;
    this.adder.edit.get('nombre').disable();
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
