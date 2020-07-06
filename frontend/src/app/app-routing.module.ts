import { Routes, RouterModule } from '@angular/router';
import { SeeComponent } from './see/see.component';
import { DeleteComponent } from './delete/delete/delete.component';
import { AdderComponent } from './adder/adder.component';
import { LogInComponent } from './log-in/log-in.component';


const APP_ROUTES: Routes = [
  { path: 'all', component: SeeComponent },
  { path: '', component: LogInComponent },
  { path: 'add', component: AdderComponent },
  { path: 'manage', component: DeleteComponent }

];

export const APP_ROUTING = RouterModule.forRoot(APP_ROUTES, {useHash: true});
