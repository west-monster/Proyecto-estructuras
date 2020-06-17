import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UndoNoUndoService } from '../../services/undo-no-undo.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(public router: Router, public history: UndoNoUndoService) { }

  ngOnInit(): void {
  }

  undo(){
    this.history.undo();
  }
  noUndo(){
    this.history.noUndo();
  }

}
