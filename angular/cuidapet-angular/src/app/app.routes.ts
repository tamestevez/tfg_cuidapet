import { Routes } from '@angular/router';
import { HomeComponent } from './public/home/home.component';
import { AdoptionsComponent } from './public/adoptions/adoptions.component';
import { AnimalInfoComponent } from './public/adoptions/animal-info.component';
import { LoginComponent } from './public/login/login.component';
import { ForgotpassComponent } from './public/forgotpass/forgotpass.component';
import { ResetpassComponent } from './public/resetpass/resetpass.component';
import { OtploginComponent } from './public/otplogin/otplogin.component';
import { PropietarioHomeComponent } from './private/propietario/home/propietario-home.component';
import { ProtectoraHomeComponent } from './private/protectora/home/protectora-home.component';
import { VeterinarioHomeComponent } from './private/veterinario/home/veterinario-home.component';
import { VetAnimalInfoComponent } from './private/veterinario/home/animal-info.component';
import { UsersVetComponent } from './private/veterinario/home/users-vet.component';
import { AdministracionHomeComponent } from './private/administracion/home/administracion-home.component';
import { UsersAdminComponent } from './private/administracion/home/users-admin.component';
import { ProtAnimalInfoComponent } from './private/protectora/home/animal-info.component';
import { PropAnimalInfoComponent } from './private/propietario/home/animal-info.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'adoptions', component:  AdoptionsComponent },
  { path: 'login', component:  LoginComponent },
  { path: 'forgotpassword', component:  ForgotpassComponent},
  { path: 'resetpassword', component:  ResetpassComponent},
  { path: 'otplogin', component:  OtploginComponent},
  { path: 'adoptions/:id', component:  AnimalInfoComponent},
  { path: 'private/prop', component:  PropietarioHomeComponent},
  { path: 'private/prop/animal/:id', component:  PropAnimalInfoComponent},
  { path: 'private/prot', component:  ProtectoraHomeComponent},
  { path: 'private/prot/animal/:id', component:  ProtAnimalInfoComponent},
  { path: 'private/vet', component:  VeterinarioHomeComponent},
  { path: 'private/vet/animal/:id', component:  VetAnimalInfoComponent},
  { path: 'private/vet/users', component:  UsersVetComponent},
  { path: 'private/admin', component:  AdministracionHomeComponent},
  { path: 'private/admin/users', component:  UsersAdminComponent},
];