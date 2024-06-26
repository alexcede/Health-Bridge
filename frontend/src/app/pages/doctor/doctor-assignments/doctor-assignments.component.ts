import { Component, OnInit } from '@angular/core';
import { DoctorHeaderComponent } from '../doctor-header/doctor-header.component';
import { TableDataComponent } from '../../../shared/components/table-data/table-data.component';
import { DoctorService } from '../../../core/services/doctor/doctor.service';
import { UserService } from '../../../core/services/user/user.service';
import { AuthService } from '../../../core/services/auth/auth.service';
import { DoctorAssignmentResult } from '../../../core/models/assignment';
import { Doctor } from '../../../core/models/doctor';
import { User } from '../../../core/models/user';
import { DoctorTableAssignmentResponse } from '../../../core/models/assignment';
import { forkJoin, Observable, of } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';
import { Action, getEntityProperties } from '../../../core/models/table-column';
import { Router } from '@angular/router';
import { AssignmentService } from '../../../core/services/assignment/assignment.service';

@Component({
  selector: 'app-doctor-assignments',
  standalone: true,
  imports: [DoctorHeaderComponent, TableDataComponent],
  templateUrl: './doctor-assignments.component.html',
  styleUrls: ['./doctor-assignments.component.css']
})
export class DoctorAssignmentsComponent implements OnInit {
  constructor(
    private doctorService: DoctorService,
    private userService: UserService,
    private authService: AuthService,
    private router: Router,
    private assignmentService: AssignmentService
  ) { }

  public doctorAssignmentList: DoctorTableAssignmentResponse[] = [];
  public columns: string[] = [];
  title: string = 'doctor assignments';
  doctor_id: number = this.authService.getUserIdFromLocalStorage();

  ngOnInit(): void {
    this.columns = ['id', 'doctor_name', 'user_name', 'dni', 'phoneNumber', 'dateCreated', 'active'];
    this.loadDoctorAssignments();
  }

  loadDoctorAssignments() {
    this.doctorService.getDoctorAssignments(this.doctor_id).pipe(
      switchMap(assignments => {
        // Create an array of observables to fetch doctor and user details
        const observables = assignments.map(assignment =>
          forkJoin({
            doctor: this.getDoctorDetails(assignment.doctor),
            user: this.getUserDetails(assignment.user),
            assignment: of(assignment)
          }).pipe(
            map(({ doctor, user, assignment }) => ({
              id: assignment.id,
              doctor: assignment.doctor.toString(),
              doctor_name: `${doctor.name} ${doctor.firstSurname} ${doctor.secondSurname}`,
              user: assignment.user.toString(),
              dni: user.dni,
              phoneNumber: user.phoneNumber,
              user_name: `${user.name} ${user.firstSurname} ${user.secondSurname}`,
              dateCreated: new Date(assignment.dateCreated).toLocaleDateString('es-ES'),
              active: assignment.active
            } as DoctorTableAssignmentResponse))
          )
        );
        return forkJoin(observables);
      })
    ).subscribe(updatedAssignments => {
      this.doctorAssignmentList = updatedAssignments;
      console.log(this.doctorAssignmentList);
    });
  }

  getDoctorDetails(doctorId: number): Observable<Doctor> {
    return this.doctorService.getDoctor(doctorId).pipe(
      map(doctor => doctor || { name: '', firstSurname: '', secondSurname: '' } as Doctor)
    );
  }

  getUserDetails(userId: number): Observable<User> {
    return this.userService.getUser(userId).pipe(
      map(user => user || { name: '', firstSurname: '', secondSurname: '' } as User)
    );
  }

  trackById(index: number, item: DoctorTableAssignmentResponse): number {
    return item.id;
  }

  delete(assignmentId: number) {
    this.assignmentService.deactivateAssignment(assignmentId).subscribe(
      response => {
        console.log(response);
        // Actualizar la lista después de la eliminación
        this.loadDoctorAssignments();
      },
      error => {
        console.error('Error deleting user:', error);
      }
    );
  }
  activate(assignmentId: number) {
    this.assignmentService.activateAssignment(assignmentId).subscribe(
      response => {
        console.log(response);

        this.loadDoctorAssignments();
      },
      error => {
        console.error('Error updating user:', error);
      }
    );
  }
  onAction(tableAction: Action) {
    if (tableAction.action === 'Edit') {
      console.log('edit' + tableAction.row.id);
    } else if (tableAction.action === 'Delete') {
      this.delete(tableAction.row.id)
    } else if (tableAction.action === 'Activate') {
      this.activate(tableAction.row.id)
    } else if (tableAction.action === 'Info') {
      const userId = tableAction.row.user;
      this.router.navigate(['/doctor/user-profile', userId]);
    }
  }
}
