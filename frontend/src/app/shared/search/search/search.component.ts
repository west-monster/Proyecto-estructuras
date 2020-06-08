import { Component, OnInit, EventEmitter, Output, Input, ViewChild } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { DataTable } from '../../../Interfaces/intefaces';
import { TableComponent } from '../../table/table/table.component';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  @ViewChild(TableComponent) table;
  @Input() text: string;
  @Input() actionFlag: number;
  public searchP: FormGroup;
  public data: DataTable[];
  constructor() {
    this.data = [{"id":0,"nombre":"varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla","precio":77,"codigoBarras":86,"cantidad":65,"fecha":"5/1/2020"},
  ];
    this.searchP = new FormGroup({
      elm: new FormControl('', Validators.required)
    });
   }

  submit(){
    console.log('data search');
  }
  sendSelected(): number[]{
    return this.table.selecterSaver;
  }
  ngOnInit(): void {
  }

}
