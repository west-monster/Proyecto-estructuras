import { Component, OnInit } from '@angular/core';
import { DataTable } from '../Interfaces/intefaces';
import elms from './data.json';
@Component({
  selector: 'app-see',
  templateUrl: './see.component.html',
  styleUrls: ['./see.component.css']
})
export class SeeComponent {

  public data: DataTable[];

  constructor() {
    this.data = elms;

  }



}
