import { Component, OnInit, ViewChild } from '@angular/core';
import { SearchComponent } from '../../shared/search/search/search.component';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit {

  @ViewChild(SearchComponent) searcher;
  constructor() {
    
   }
   

  ngOnInit(): void {
  }

}
