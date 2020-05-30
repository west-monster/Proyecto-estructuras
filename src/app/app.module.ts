import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { FooterComponent } from './shared/footer/footer.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import { APP_ROUTING } from './app-routing.module';
import { SeeComponent } from './see/see.component';
import { TableComponent } from './shared/table/table/table.component';
import { AddComponent } from './add/add/add.component';
import { SearchOpComponent } from './search/search/search.component';
import { DeleteComponent } from './delete/delete/delete.component';
import { SearchComponent } from './shared/search/search/search.component';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    NavbarComponent,
    SeeComponent,
    TableComponent,
    AddComponent,
    SearchOpComponent,
    DeleteComponent,
    SearchComponent
  ],
  imports: [
    BrowserModule,
    APP_ROUTING,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
