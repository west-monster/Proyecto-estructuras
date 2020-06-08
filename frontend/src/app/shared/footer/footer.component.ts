import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent {
  public names: string[];
  public mails: string[];

  constructor() {
    this.names = [' Juan Sanchez,', ' Santiago Pardo,', ' Antonio Garzon,'];
    this.mails = ['jusanchez@unal.edu.co', 'dpardogo@unal.edu.co', 'dgarzona@unal.edu.co'];
    this.setNames();
  }
  setNames(){
    let ranIndex: number;
    let aux: string;
    let auxE: string;
    for (let i = 0; i < 3; i++) {
      ranIndex = Math.round(Math.random() * 2);
      aux = this.names[i];
      auxE = this.mails[i];
      this.names[i] = this.names[ranIndex];
      this.mails[i] = this.mails[ranIndex];
      this.names[ranIndex] = aux;
      this.mails[ranIndex] = auxE;
    }
    this.names[2] = this.names[2].slice(0, -1);
  }

}
