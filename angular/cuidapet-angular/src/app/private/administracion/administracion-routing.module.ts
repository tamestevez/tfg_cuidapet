import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdministracionHomeComponent } from './home/administracion-home.component';
import { UsersAdminComponent } from './home/users-admin.component';

const routes: Routes = [
  { path: '/admin', component: AdministracionHomeComponent }
  { path: '/admin/users', component: UsersAdminComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdministracionRoutingModule { }