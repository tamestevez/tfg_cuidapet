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
export class VetAnimalInfoComponent implements OnInit {
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
      vaccines: [
        { tipo: 'Rabia', date: new Date('2023-01-15'), fabricante: 'Fabricante A' },
        { tipo: 'Polivalente', date: new Date('2023-02-20'), fabricante: 'Fabricante B' }
      ],
      treatments: [
        { name: 'Desparasitación', fabricante: 'Fabricante A', dosis: '10mg', frequency: 'trimestral' },
      ],
      diseases: [
        { name: 'Ninguna' }
      ],
      surgeries: [
        { name: 'Esterilización', fecha: new Date('2021-05-10'), observaciones: 'Procedimiento exitoso' }
      ]
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
      vaccines: [
        { tipo: 'Rabia', date: new Date('2023-01-10'), fabricante: 'Fabricante C' },
        { tipo: 'Moquillo', date: new Date('2023-02-05'), fabricante: 'Fabricante D' }
      ],
      treatments: [
        { name: 'Vitaminas', fabricante: 'Fabricante B', dosis: '5ml', frequency: 'mensual' }
      ],
      diseases: [
        { name: 'Alergia', description: 'a ciertos alimentos' }
      ],
      surgeries: [
        { name: 'Operación de rodilla', fecha: new Date('2020-03-15'), observaciones: 'Recuperación en curso' }
      ]
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
      vaccines: [
        { tipo: 'Rabia', date: new Date('2023-01-20'), fabricante: 'Fabricante E' },
        { tipo: 'Leptospirosis', date: new Date('2023-03-01'), fabricante: 'Fabricante F' }
      ],
      treatments: [
        { name: 'Desparasitación', fabricante: 'Fabricante A', dosis: '10mg', frequency: 'trimestral' },
      ],
      diseases: [
        { name: 'Otitis', description: 'recurrente' }
      ],
      surgeries: [
        { name: 'Ninguna', fecha: null, observaciones: 'No ha requerido cirugía' }
      ]
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