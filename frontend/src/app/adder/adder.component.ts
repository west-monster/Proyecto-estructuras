import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { AddComponent } from '../shared/add/add.component';
import { ConnectionService } from '../services/connection.service';
import { DomSanitizer } from '@angular/platform-browser';
import { HttpEventType } from '@angular/common/http';
import { Recomendations } from '../Interfaces/intefaces';

@Component({
  selector: 'app-adder',
  templateUrl: './adder.component.html',
  styleUrls: ['./adder.component.css']
})
export class AdderComponent implements OnInit, AfterViewInit {
  @ViewChild(AddComponent) adder;
  private loadChild: boolean;
  public file: File;
  public fileUrl: any;
  public notAdmit: boolean;

  public sending: boolean;
  public errorUpload: boolean;
  public progress: string;

  public recomendations: Recomendations[];
  constructor(private conn: ConnectionService, public domS: DomSanitizer) {
    this.loadChild = false;
    this.file = null;
    this.fileUrl = null;
    this.notAdmit = false;
    this.sending = false;
    this.errorUpload = false;
    this.progress = '';
    this.recomendations = [];
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

  addFileGroup(event) {
    let auxType: string;

    auxType = event.target.files[0].name.substring(event.target.files[0].name.indexOf('.')).toLowerCase();
    if (auxType === '.png' || auxType === '.jpeg' || auxType === '.jpg') {

      this.file = event.target.files[0];

      this.fileUrl = this.domS.bypassSecurityTrustResourceUrl(URL.createObjectURL(event.target.files[0]));
      this.notAdmit = false;

    } else {
      this.notAdmit = true;
    }

    console.log(this.file);
  }
  removeFile() {
    this.file = null;
    this.notAdmit = false;
    console.log(this.file);
  }

  detecteItem() {

    const formData = new FormData();
    formData.append('file', this.file, 'img' + this.file.name.substring(this.file.name.indexOf('.')).toLowerCase());

    this.sending = true;
    this.conn.detecteItem(formData).subscribe((events) => {
        if (events.type === HttpEventType.UploadProgress) {
          const auxProgress = Math.round(events.loaded / events.total * 100);
          if (auxProgress === 100) {
            this.progress = 'Procesando';
          } else {
            this.progress = 'Subiendo: ' + auxProgress.toString() + '%';
          }
        } else if (events.type === HttpEventType.Response) {
          // tslint:disable-next-line:no-string-literal
          if (!(events.body['query'])) {
            this.errorUpload = true;
            this.recomendations = [];
          } else {
            this.progress = 'Guardado exitosamente.';
            // tslint:disable-next-line:no-string-literal
            this.recomendations = events.body['ans'];
          }
          this.sending = false;
        }
     });
  }

  loadName(index: number){
    this.adder.edit.get('nombre').setValue(this.recomendations[index].description);
  }

}
