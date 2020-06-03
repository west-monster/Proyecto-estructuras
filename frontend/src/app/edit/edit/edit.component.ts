import { Component, OnInit, ViewChild, OnDestroy } from '@angular/core';
import { SearchComponent } from '../../shared/search/search/search.component';
import { DataTable } from '../../Interfaces/intefaces';
import { EditService } from './edit.service';
import { Subscription } from 'rxjs';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { formatDate } from '@angular/common';
import { AddComponent } from '../../shared/add/add.component';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnDestroy {


  @ViewChild(SearchComponent) searcher;
  @ViewChild(AddComponent) adder;
  private subscription: Subscription;
  private idEdit: number;
  constructor(public shareAux: EditService) {
    this.idEdit = null;
    this.subscription = this.shareAux.triggerEdit$.subscribe(
      id => {
        console.log(id);
        this.load(id);
    });
  }

  load(id: number){
    this.adder.edit.reset(this.searcher.data[id]);
    const date: Date = new Date(this.searcher.data[id].fecha);
    this.adder.edit.get('fecha').setValue(formatDate(date, 'yyyy-MM-dd', 'en'));
    this.idEdit = id;
  }
  submit(){
    const aux = this.adder.edit.value;
    aux.id = this.idEdit;
    console.log(aux);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
