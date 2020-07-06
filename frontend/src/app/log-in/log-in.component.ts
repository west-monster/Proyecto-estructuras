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
  this.conn.logIn(this.form.get('user').value, this.form.get('pass').value).subscribe((ans) => {
      if (ans) {
        this.flagLog = false;
        this.router.navigate(['/all']);
      } else {
        this.flagLog = true;
        this.error = 'Clave o usuario incorrectos';
        this.form.reset({
          user: this.form.get('user').value,
          pass: ''
        });
      }
      this.validing = false;
    
  });

 }

}
