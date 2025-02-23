import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VeterinarioHomeComponent } from './veterinario-home.component';

describe('VeterinarioHomeComponent', () => {
  let component: VeterinarioHomeComponent;
  let fixture: ComponentFixture<VeterinarioHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VeterinarioHomeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VeterinarioHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
