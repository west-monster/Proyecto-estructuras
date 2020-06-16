import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { AddComponent } from '../shared/add/add.component';
import { ConnectionService } from '../services/connection.service';

@Component({
  selector: 'app-adder',
  templateUrl: './adder.component.html',
  styleUrls: ['./adder.component.css']
})
export class AdderComponent implements OnInit, AfterViewInit {
  @ViewChild(AddComponent) adder;
  private loadChild: boolean;
  constructor(private conn: ConnectionService) {
    this.loadChild = false;
   }

  ngOnInit(): void {
  }
  get valid(){
    return this.loadChild ? this.adder.edit.valid : false;
  }

  ngAfterViewInit(){
    this.loadChild = true;
  }
  submit(){
    this.conn.add(this.adder.edit.value).subscribe((ans: boolean) => {
      
    });
  }

}
