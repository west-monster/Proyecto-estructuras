import { Component, OnInit, Input, ViewChild, AfterViewInit } from '@angular/core';
import { DataTable } from '../../Interfaces/intefaces';
import { SearchComponent } from '../../shared/search/search/search.component';
declare var $: any;

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements AfterViewInit {

  @ViewChild(SearchComponent) searcher;
  private childLoad: boolean;
  constructor(){
    this.childLoad = false;
  }
  delete(){
    const toDelete: number[] = this.searcher.sendSelected();
    console.log(toDelete);
  }
  deleteAllModal(){
    $('#modalDeleteAll').modal();
  }
  get data(){
    return this.childLoad ?  this.searcher.table.selecterSaver.length : 0;
  }
  deleteAll(){
    $('#modalDeleteAll').modal('hide');
  }

  ngAfterViewInit(): void {
    this.childLoad = true;
  }

}
