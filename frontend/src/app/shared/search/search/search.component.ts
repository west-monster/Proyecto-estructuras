import { Component, OnInit, EventEmitter, Output, Input, ViewChild } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { DataTable } from '../../../Interfaces/intefaces';
import { TableComponent } from '../../table/table/table.component';
import { ConnectionService } from '../../../services/connection.service';

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
  constructor(private conn: ConnectionService) {
    this.searchP = new FormGroup({
      elm: new FormControl('', Validators.required)
    });
   }

  submit(){
    this.conn.search(this.searchP.get('elm').value).subscribe((ans: DataTable[]) => {
      this.table.setDataL(ans);
      console.log(ans);
    });
  }
  sendSelected(): number[]{
    return this.table.selecterSaver;
  }
  ngOnInit(): void {
  }

}
