import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProtectoraHomeComponent } from './protectora-home.component';

describe('ProtectoraHomeComponent', () => {
  let component: ProtectoraHomeComponent;
  let fixture: ComponentFixture<ProtectoraHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProtectoraHomeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ProtectoraHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
