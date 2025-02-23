import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-adoptions',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './adoptions.component.html',
  styleUrl: './adoptions.component.css'
})

export class AdoptionsComponent implements OnInit {
  animales = [
    { id: 1, name: 'Luna', tipo:'Gato', sex:'Hembra', town: 'Madrid', date: '10/12/2022', image: 'assets/logo-icon.png' },
    { id: 2, name: 'Max',  tipo:'Perro', sex:'Macho', town: 'Barcelona', date: '13/10/2021', image: 'assets/logo-icon.png' },
    { id: 3, name: 'Bella',  tipo:'Pajaro', sex:'Hembra', town: 'Valencia', date: '08/07/2019', image: 'assets/logo-icon.png' }
  ];

tiposAnimales: string[] = [];
filtroTipoAnimal: string = '';

townsDisponible: string[] = [];
filtroTown: string = '';

animalesFiltrados = [...this.animales];

constructor() {}

ngOnInit() {
  this.tiposAnimales = [...new Set(this.animales.map(animal => animal.tipo))];
  this.townsDisponible = [...new Set(this.animales.map(animal => animal.town))];
}

filtrarAnimales() {
  this.animalesFiltrados = this.animales.filter(animal => {
    const filtroTipo = this.filtroTipoAnimal ? animal.tipo === this.filtroTipoAnimal : true;
    const filtroTown = this.filtroTown ? animal.town === this.filtroTown : true;
    return filtroTipo && filtroTown;
  });
}
}

