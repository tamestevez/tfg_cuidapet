import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PropietarioHomeComponent } from './home/propietario-home.component';

const routes: Routes = [
  { path: '', component: PropietarioHomeComponent } // Ruta base
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PropietarioRoutingModule { }