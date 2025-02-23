import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProtectoraHomeComponent } from './home/protectora-home.component';

const routes: Routes = [
  { path: '', component: ProtectoraHomeComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProtectoraRoutingModule { }
