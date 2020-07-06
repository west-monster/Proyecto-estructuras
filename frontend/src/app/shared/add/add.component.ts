import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { formatDate } from '@angular/common';
@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit{

  public edit: FormGroup;

  constructor() {
    this.edit = new FormGroup({
      nombre: new FormControl('', Validators.required),
      precio: new FormControl('', [Validators.pattern('^[0-9.,]*$'), Validators.required]),
      codigo: new FormControl('', [Validators.pattern('^[0-9.,]*$'), Validators.required]),
      cantidad: new FormControl('', [Validators.pattern('^[0-9.,]*$'), Validators.required]),
      fecha: new FormControl('', Validators.required),
    });
  }
  
  ngOnInit(): void {
    this.edit.get('fecha').setValue(formatDate(new Date(), 'yyyy-MM-dd', 'en'));
  }

  submit(){
  }


}
