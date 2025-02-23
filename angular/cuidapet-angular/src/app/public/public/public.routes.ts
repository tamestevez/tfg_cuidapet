import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AdoptionsComponent } from './adoptions/adoptions.component';
import { AnimalInfoComponent } from './adoptions/animal-info.component';
import { LoginComponent } from './login/login.component';
import { ForgotpassComponent } from './forgotpass/forgotpass.component';
import { ResetpassComponent } from './resetpass/resetpass.component';
import { OtploginComponent } from './otplogin/otplogin.component';

export const PUBLIC_ROUTES: Routes = [
  { path: '', component: HomeComponent }
  { path: '/adoptions', component: AdoptionsComponent }
  { path: '/login', component: LoginComponent }
  { path: '/forgotpassword', component: ForgotpassComponent }
  { path: '/resetpassword', component: ResetpassComponent }
  { path: '/otplogin', component: OtploginComponent }
  { path: '/adoptions/:id', component: AnimalInfoComponent }

];
