import { Component, OnInit, Input, ViewChild, AfterViewInit } from '@angular/core';
import { DataTable } from '../../Interfaces/intefaces';
import { SearchComponent } from '../../shared/search/search/search.component';
import { ConnectionService } from '../../services/connection.service';
declare var $: any;

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements AfterViewInit {

  @ViewChild(SearchComponent) searcher;
  private childLoad: boolean;
  constructor(private conn: ConnectionService){
    this.childLoad = false;
  }
  delete(){
    this.conn.delete(this.searcher.sendSelected()).subscribe((ans: boolean) => {
      ans ? console.log(1) : console.log(0);
      this.searcher.submit();
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
