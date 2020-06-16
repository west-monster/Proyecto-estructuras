import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { DataTable } from '../../../Interfaces/intefaces';
import { EditService } from '../../../edit/edit/edit.service';
import { ConnectionService } from '../../../services/connection.service';
declare var $: any;
@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit{

  public data: DataTable[];
  public totalResults: number;
  @Input() queryTarget: string;
  @Input() actionFlag: boolean;
  public typeOrder: number;
  public selecterSaver: string[];
  public firstId: number;
  public keys: string[];
  public showAllF: boolean;
  public limit: number;
  public totalPages: number;
  public currentPage: number;

  constructor(public shareAux: EditService, private conn: ConnectionService) {
    this.actionFlag = false;
    this.typeOrder = 0;
    this.totalResults = 0;
    this.selecterSaver = [];
    this.data = [];
    this.firstId = 0;
    this.keys = ['nombre', 'precio', 'codigo', 'cantidad', 'fecha'];
    this.showAllF = false;
    this.currentPage = 0;
    this.limit = 0;
  }
  ngOnInit(): void {
    if (this.queryTarget === 'seeAll') {
      this.setPages(25);
      this.setData();
    }
  }

  addSelected(index: number){
    const pos = this.selecterSaver.indexOf(this.data[index].nombre);
    if (pos === -1){
       this.selecterSaver.push(this.data[index].nombre);
    } else if (pos !== -1){
      this.selecterSaver.splice(pos, 1);
    }
  }

  triggerEdit(id: number){
    this.shareAux.snedId(id);
  }

  showAll(){
    this.showAllF = !this.showAllF;
    this.showAllF ?  this.setPages(this.totalResults) : this.setPages(25);
    this.setData();
    $('#modalLoadAll').modal('hide');
  }
  showModal(){
    if (this.limit !== this.totalResults){
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
      this.totalPages = Math.round(this.totalResults / this.limit);
      this.currentPage = Math.floor((this.currentPage * aux  + 1) / this.limit);
    }
    this.firstId = this.currentPage * this.limit;
  }
  setData(){
    // this.firstId should be this.data[-1].id (last id of the last element)

        this.conn.seeAll(this.firstId, this.limit).subscribe((ans: DataTable[]) => {
          this.data = ans;
          this.totalResults = ans.length;
          this.totalPages = Math.round(this.totalResults / this.limit);
          this.firstId = this.currentPage * this.limit;
        });


  }
  setDataL(ans: DataTable[]){
    this.setPages(25);
    this.data = ans;
    this.data = ans;
    this.totalResults = ans.length;
    this.totalPages = Math.round(this.totalResults / this.limit);
    this.firstId = this.currentPage * this.limit;
  }
  setLimit(value?: Event){
    // tslint:disable-next-line:no-string-literal
    if (value.target['value'] !== -1) {
      this.showAllF = false;
      // tslint:disable-next-line:no-string-literal
      this.setPages(value.target['value']);
      this.setData();
    }
  }
  setTypeOrder(value?: Event){
    // tslint:disable-next-line:no-string-literal
    this.typeOrder = value.target['value']; console.log(value.target['value']);

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
    this.firstId = this.currentPage * this.limit;
    this.setData();
  }

}
