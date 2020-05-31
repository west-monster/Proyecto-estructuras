import { Routes, RouterModule } from '@angular/router';
import { SeeComponent } from './see/see.component';
import { AddComponent } from './add/add/add.component';
import { SearchOpComponent } from './search/search/search.component';
import { DeleteComponent } from './delete/delete/delete.component';


const APP_ROUTES: Routes = [
  { path: '', component: SeeComponent },
  { path: 'add', component: AddComponent },
  { path: 'search', component: SearchOpComponent },
  { path: 'delete', component: DeleteComponent }

];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES, {useHash: true});
