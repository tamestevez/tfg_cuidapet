import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-veterinario-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './users-vet.component.html',
  styleUrl: './users-vet.component.css'
})
export class UsersVetComponent {
    usuarios = [
        { nombre: 'Juan Pérez', rol: 'Propietario', email: 'juan@example.com', phone:'123456789'},
        { nombre: 'María López', rol: 'Propietario', email: 'maria@example.com', phone:'123456789' },
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

  filtro: string = '';
  usuariosFiltrados = [...this.usuarios];

  filtrarUsuarios(event: Event): void {
    const inputElement = event.target as HTMLInputElement; // Casting correcto
    this.filtro = inputElement.value; // Extrae el valor del input
  
    this.usuariosFiltrados = this.usuarios.filter(usuario =>
      usuario.nombre.toLowerCase().includes(this.filtro.toLowerCase()) ||
      usuario.email.toLowerCase().includes(this.filtro.toLowerCase())
    );
  }
  

}
