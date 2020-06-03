import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { DataTable } from '../../../Interfaces/intefaces';
import { EditService } from '../../../edit/edit/edit.service';
declare var $: any;
@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit{

  @Input() data: DataTable[];
  @Input() actionFlag: boolean;
  public selecterSaver: number[];
  public firstId: number;
  public keys: string[];
  public currentData: DataTable[];
  public showAllF: boolean;
  public limit: number;
  public totalPages: number;
  public currentPage: number;

  constructor(public shareAux: EditService) {
    this.actionFlag = false;
    this.selecterSaver = [];
    this.firstId = 0;
    this.keys = ['nombre', 'precio', 'codigoBarras', 'cantidad', 'fecha'];
    this.showAllF = false;
    this.currentPage = 0;
    this.limit = 0;
  }
  ngOnInit(): void {
    this.setPages(25);
  }
  addSelected(index: number){
    const pos = this.selecterSaver.indexOf(index);
    if (pos === -1){
       this.selecterSaver.push(index);
    } else if (pos !== -1){
      this.selecterSaver.splice(pos, 1);
    }
  }

  triggerEdit(id: number){
    this.shareAux.snedId(id);
  }

  showAll(){
    this.showAllF = !this.showAllF;
    this.showAllF ?  this.setPages(-1) : this.setPages(25);
    $('#modalLoadAll').modal('hide');
  }
  showModal(){
    if (this.limit !== -1){
      $('#modalLoadAll').modal();
    } else{
      this.showAll();
    }
  }
  setPages(NLimit: number){
    const aux = this.limit;
    this.limit = NLimit;
    if (this.showAllF) {
      this.totalPages = 0;
      this.currentPage =  0;
    } else {
      this.totalPages = Math.round(this.data.length / this.limit) - 1;
      this.currentPage = Math.floor((this.currentPage * aux  + 1) / this.limit);
    }
    this.firstId = this.currentPage * this.limit;
    this.movePage();
  }
  setLimit(value?: Event){
    // tslint:disable-next-line:no-string-literal
    if (value.target['value'] !== -1) {
      this.showAllF = false;
      // tslint:disable-next-line:no-string-literal
      this.setPages(value.target['value']);
    }
  }
  movePage(action: number = 0){
    if (action === 1 && this.currentPage < this.totalPages) {
      this.currentPage ++;
    } else if (action === -1 && this.currentPage > 0) {
      this.currentPage--;
    } else if (action === 2 && this.currentPage < this.totalPages) {
      this.currentPage = this.totalPages;
    } else if (action === -2 && this.currentPage > 0) {
      this.currentPage = 0;
    }
    this.currentData = this.data.slice(this.currentPage * this.limit, (this.currentPage + 1) * this.limit);
  }

}
