import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-administracion-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './users-admin.component.html',
  styleUrl: './administracion-home.component.css'
})
export class UsersAdminComponent {
    usuarios = [
        { nombre: 'Juan Pérez', rol: 'Administrador', email: 'juan@example.com', phone:'123456789'},
        { nombre: 'María López', rol: 'Veterinario', email: 'maria@example.com', phone:'123456789' },
        { nombre: 'Carlos Gómez', rol: 'Propietario', email: 'carlos@example.com', phone:'123456789' }
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
