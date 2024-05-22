import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorAssignmentsComponent } from './doctor-assignments.component';

describe('DoctorAssignmentsComponent', () => {
  let component: DoctorAssignmentsComponent;
  let fixture: ComponentFixture<DoctorAssignmentsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DoctorAssignmentsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DoctorAssignmentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
