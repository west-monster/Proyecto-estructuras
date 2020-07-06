import { Component, OnInit } from '@angular/core';
import { ConnectionService } from '../services/connection.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent {

  public form: FormGroup;
  public flagLog: boolean;
  public error: string;
  public validing: boolean;

 constructor(private conn: ConnectionService, public router: Router) {
   this.flagLog = false;
   this.error = '';
   this.validing = false;
   this.form = new FormGroup({
     user: new FormControl('', Validators.required),
     pass: new FormControl('', Validators.required)
     });
 }
 submit() {


 }
 setSessionToken(value: any) {
   const h: boolean = value.query;
   const y: string = value.token;
   if (h) {
     this.flagLog = false;
     sessionStorage.setItem('session', y);
     if (!value.state) {
       this.router.navigate(['/expired']);
     }
   } else {
     this.flagLog = true;
     this.error = 'Ups. Try again.';
     this.form.reset({
       user: this.form.get('user').value,
       pass: ''
     });
   }
   this.validing = false;
 }

}
