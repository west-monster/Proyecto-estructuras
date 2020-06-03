import { Routes, RouterModule } from '@angular/router';
import { SeeComponent } from './see/see.component';
import { SearchOpComponent } from './search/search/search.component';
import { DeleteComponent } from './delete/delete/delete.component';
import { EditComponent } from './edit/edit/edit.component';
import { AdderComponent } from './adder/adder.component';


const APP_ROUTES: Routes = [
  { path: '', component: SeeComponent },
  { path: 'add', component: AdderComponent },
  { path: 'edit', component: EditComponent },
  { path: 'search', component: SearchOpComponent },
  { path: 'delete', component: DeleteComponent }

];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES, {useHash: true});
