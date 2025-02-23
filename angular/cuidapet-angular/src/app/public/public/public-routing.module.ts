import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AdoptionsComponent } from './adoptions/adoptions.component';
import { AnimalInfoComponent } from './adoptions/animal-info.component';
import { LoginComponent } from './login/login.component';
import { ForgotpassComponent } from './forgotpass/forgotpass.component';
import { ResetpassComponent } from './forgotpass/forgotpass.component';
import { OtploginComponent } from './otplogin/otplogin.component';

const routes: Routes = [{ path: '', component: HomeComponent }];
const routes: Routes = [{ path: '/adoptions', component: AdoptionsComponent }];
const routes: Routes = [{ path: '/adoptions/:id', component: AnimalInfoComponent }];
const routes: Routes = [{ path: '/login', component: LoginComponent }];
const routes: Routes = [{ path: '/forgotpassword', component: ForgotpassComponent }];
const routes: Routes = [{ path: '/resetpassword', component: ResetpassComponent }];
const routes: Routes = [{ path: '/otplogin', component: OtploginComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicRoutingModule { }