import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-animal-info',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './animal-info.component.html',
  styleUrls: ['./animal-info.component.css']
})
export class ProtAnimalInfoComponent implements OnInit {
  animal: any;
  selectedTab: string = 'general';
  
  animales = [
    { 
      id: 1, 
      name: 'Luna', 
      sex: 'Hembra', 
      town: 'Madrid', 
      date: '10/12/2022', 
      image: 'assets/logo-icon.png', 
      traits: 'Juguetona, cariñosa', 
      color: 'Negro', 
      breed: 'Labrador', 
      species: 'Perro', 
      ppp: 'No',
      chip: '123456789', 
      passport: 'ESP123456',
      vaccines: ['Rabia 2023', 'Polivalente 2023'],
      treatments: ['Desparasitación trimestral'],
      diseases: ['Ninguna'],
      surgeries: ['Esterilización 2021']
    },
    { 
      id: 2, 
      name: 'Max', 
      sex: 'Macho', 
      town: 'Barcelona', 
      date: '13/10/2021', 
      image: 'assets/logo-icon.png', 
      traits: 'Tranquilo y leal', 
      color: 'Marrón', 
      breed: 'Golden Retriever', 
      species: 'Perro', 
      ppp: 'No',
      chip: '987654321', 
      passport: 'ESP654321',
      vaccines: ['Rabia 2023', 'Moquillo 2023'],
      treatments: ['Vitaminas para articulaciones'],
      diseases: ['Alergia a ciertos alimentos'],
      surgeries: ['Operación de rodilla 2020']
    },
    { 
      id: 3, 
      name: 'Bella', 
      sex: 'Hembra', 
      town: 'Valencia', 
      date: '08/07/2019', 
      image: 'assets/logo-icon.png', 
      traits: 'Energética y amorosa', 
      color: 'Blanco con manchas', 
      breed: 'Dálmata', 
      species: 'Perro', 
      ppp: 'No',
      chip: '456789123', 
      passport: 'ESP789123',
      vaccines: ['Rabia 2023', 'Leptospirosis 2023'],
      treatments: ['Desparasitación anual'],
      diseases: ['Otitis recurrente'],
      surgeries: ['Ninguna']
    }
  ];

  constructor(private route: ActivatedRoute, private router: Router) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.animal = id ? this.animales[+id-1] : null;
  }

  changeTab(tab: string) {
    this.selectedTab = tab;
  }

  menuOpen = false;

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