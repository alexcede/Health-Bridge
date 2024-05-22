import { Routes } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { DoctorAssignmentsComponent } from "./doctor-assignments/doctor-assignments.component";
import { DoctorUserProfileComponent } from "./doctor-user-profile/doctor-user-profile.component";

export const DOCTOR_ROUTES: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
  },
  {
    path: 'assignments',
    component: DoctorAssignmentsComponent,
  },
  {
    path: 'user-profile/:id',
    component: DoctorUserProfileComponent,
  }
];
