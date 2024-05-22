import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorUserRecipeListComponent } from './doctor-user-recipe-list.component';

describe('DoctorUserRecipeListComponent', () => {
  let component: DoctorUserRecipeListComponent;
  let fixture: ComponentFixture<DoctorUserRecipeListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DoctorUserRecipeListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DoctorUserRecipeListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
