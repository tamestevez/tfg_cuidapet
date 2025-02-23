import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PropietarioHomeComponent } from './propietario-home.component';

describe('PropietarioHomeComponent', () => {
  let component: PropietarioHomeComponent;
  let fixture: ComponentFixture<PropietarioHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PropietarioHomeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PropietarioHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
