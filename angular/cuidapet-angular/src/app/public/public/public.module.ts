import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { AdoptionsComponent } from './adoptions/adoptions.component';
import { AnimalInfoComponent } from './adoptions/animal-info.component';
import { LoginComponent } from './login/login.component';
import { ForgotpassComponent } from './forgotpass/forgotpass.component';
import { ResetpassComponent } from './resetpass/resetpass.component';
import { OtploginComponent } from './otplogin/otplogin.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    HomeComponent,
    AdoptionsComponent, 
    LoginComponent, 
    ForgotpassComponent, 
    ResetpassComponent,
    OtploginComponent,
    AnimalInfoComponent,
  ],
  imports: [CommonModule, RouterModule],
  exports: [
    HomeComponent,
    AdoptionsComponent, 
    LoginComponent, 
    ForgotpassComponent, 
    ResetpassComponent,
    OtploginComponent,
    AnimalInfoComponent
  ]
})
export class PublicModule { }