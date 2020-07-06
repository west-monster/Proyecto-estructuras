import { Component, ViewChild } from '@angular/core';
import { DeleteComponent } from '../delete/delete/delete.component';
import { formatDate } from '@angular/common';
import { TableComponent } from '../shared/table/table/table.component';
import { FormControl } from '@angular/forms';
declare var $: any;
@Component({
  selector: 'app-see',
  templateUrl: './see.component.html',
  styleUrls: ['./see.component.css']
})
export class SeeComponent  extends DeleteComponent{
  @ViewChild(TableComponent) table;
  load(id: number){
    this.adder.edit.reset(this.table.data[id]);
    const date: Date = new Date(this.table.data[id].fecha);
    this.adder.edit.get('fecha').setValue(formatDate(date, 'yyyy-MM-dd', 'en'));
    this.idEdit = id;
  }

  top(control: FormControl){
    return (this.childLoad && control.value > this.table.data[this.idEdit].cantidad) ? { big: true } : null  ;
  }

  submit(){
    this.adder.edit.get('nombre').enable();
    const aux = this.adder.edit.value;
    aux.id = this.table.data[this.idEdit].id;
    console.log(aux);
    this.conn.edit(aux).subscribe((ans: boolean) => {
      this.table.setData();
      this.adder.edit.get('nombre').disable();
      this.history.addAction({
        type: 0,
        past: [this.table.data[this.idEdit]],
        new: [aux]
      });
      $('#modalAdd').modal('hide');
    });
  }

  sell(){
    console.log(this.table.data[this.idEdit]);
    const aux = this.table.data[this.idEdit];
    if (this.table.data[this.idEdit].cantidad < this.sold.get('tar').value) {
      aux.cantidad = 0 ;
    } else{
      aux.cantidad  = this.table.data[this.idEdit].cantidad - this.sold.get('tar').value;
    }
    console.log(aux);
    this.conn.edit(aux).subscribe((ans: boolean) => {
      this.table.setData();
      this.history.addAction({
        type: 0,
        past: [this.table.data[this.idEdit]],
        new: [aux]
      });
      $('#sellModal').modal('hide');
    });
  }

}
