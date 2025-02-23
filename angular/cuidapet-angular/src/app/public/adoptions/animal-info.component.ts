import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-animal-info',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './animal-info.component.html',
  styleUrls: ['./animal-info.component.css']
})
export class AnimalInfoComponent implements OnInit {
  animal: any;
  
  animales = [
    { id: 1, name: 'Luna', sex:'Hembra', town: 'Madrid', date: '10/12/2022', image: 'assets/logo-icon.png', traits: 'Juguetona, cariñosa',  },
    { id: 2, name: 'Max', sex:'Macho', town: 'Barcelona', date: '13/10/2021', image: 'assets/logo-icon.png', traits: 'Tranquilo y leal', },
    { id: 3, name: 'Bella', sex:'Hembra', town: 'Valencia', date: '08/07/2019', image: 'assets/logo-icon.png',  traits: 'Energética y amorosa', }
  ];

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.animal = id ? this.animales[+id-1] : null;
  }
}
