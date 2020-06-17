import { Component, OnInit, Input, ViewChild, AfterViewInit } from '@angular/core';
import { DataTable } from '../../Interfaces/intefaces';
import { SearchComponent } from '../../shared/search/search/search.component';
import { ConnectionService } from '../../services/connection.service';
import { UndoNoUndoService } from '../../services/undo-no-undo.service';
declare var $: any;

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements AfterViewInit {

  @ViewChild(SearchComponent) searcher;
  private childLoad: boolean;
  constructor(private conn: ConnectionService, public history: UndoNoUndoService){
    this.childLoad = false;
  }
  delete(){
    let aux: string[] = [];
    let historyAction: DataTable[] = [];
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
  }

}
