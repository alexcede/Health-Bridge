import { Routes } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { DoctorAssignmentsComponent } from "./doctor-assignments/doctor-assignments.component";

export const DOCTOR_ROUTES: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
  },
  {
    path: 'assignments',
    component: DoctorAssignmentsComponent,
  }
];
