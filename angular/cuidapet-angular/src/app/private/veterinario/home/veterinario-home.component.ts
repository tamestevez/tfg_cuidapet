import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-veterinario-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './veterinario-home.component.html',
  styleUrl: './veterinario-home.component.css'
})
export class VeterinarioHomeComponent {

  animales = [
    { id:1, nombre: 'Max', tipo: 'Perro', raza: 'Labrador', prop: 'Pedro Martínez', phone: '123456789' },
    { id:2, nombre: 'Milo', tipo: 'Gato', raza: 'Siames', prop: 'Lucas Jiménez', phone: '123456789' },
    { id:3, nombre: 'Luna', tipo: 'Perro', raza: 'Golden Retriever', prop: 'Patitas Peludas', phone: '123456789' }
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
