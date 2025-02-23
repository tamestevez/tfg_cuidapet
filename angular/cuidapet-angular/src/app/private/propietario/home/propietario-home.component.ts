import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';


@Component({
  selector: 'app-propietario-home',
  standalone: true,
  imports: [CommonModule,],
  templateUrl: './propietario-home.component.html',
  styleUrl: './propietario-home.component.css'
})
export class PropietarioHomeComponent {
  animales = [
    { id: 1, name: 'Luna', tipo:'Gato', sex:'Hembra', town: 'Madrid', date: '10/12/2022', image: 'assets/logo-icon.png' },
    { id: 2, name: 'Max',  tipo:'Perro', sex:'Macho', town: 'Barcelona', date: '13/10/2021', image: 'assets/logo-icon.png' },
    { id: 3, name: 'Bella',  tipo:'Pajaro', sex:'Hembra', town: 'Valencia', date: '08/07/2019', image: 'assets/logo-icon.png' }
  ];

  menuOpen = false;

  constructor(private router: Router) {}

  logout() {
    // Aquí puedes agregar lógica adicional como limpiar el almacenamiento local
    console.log('Cerrando sesión...');
    this.router.navigate(['/login']); // Redirige al login
  }

  deleteAccount() {
    const confirmDelete = confirm('¿Estás seguro de que deseas eliminar tu cuenta? Esta acción no se puede deshacer.');
    if (confirmDelete) {
      alert('Cuenta eliminada');
      this.logout();
    }
  }

  contactSupport() {
    alert('Redirigiendo a soporte...');
  }

  toggleMenu() {
    this.menuOpen = !this.menuOpen;
  }

  goToProfile() {
    this.router.navigate(['/private/propietario/perfil']);
  }

  changePassword() {
    this.router.navigate(['/private/propietario/cambiar-contrasena']);
  }

}
