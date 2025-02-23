import { Component } from '@angular/core';
import Chart from 'chart.js/auto';
import { Router } from '@angular/router';

@Component({
  selector: 'app-administracion-home',
  standalone: true,
  imports: [],
  templateUrl: './administracion-home.component.html',
  styleUrl: './administracion-home.component.css'
})
export class AdministracionHomeComponent {
  ngAfterViewInit() {
    this.renderChart();
  }

  renderChart() {
    const ctx = document.getElementById('adoptionChart') as HTMLCanvasElement;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
        datasets: [{
          label: 'Adopciones',
          data: [40, 30, 45, 50, 35, 60],
          backgroundColor: 'rgba(138, 43, 226, 0.6)', 
          borderRadius: 5
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
  }

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
