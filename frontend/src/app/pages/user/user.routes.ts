import { Routes } from '@angular/router';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { UserAssignmentsComponent } from './user-assignments/user-assignments.component';

export const USER_ROUTES: Routes = [
  {
    path: ':id',
    component: UserProfileComponent
  },
  {
    path: 'assignments',
    component: UserAssignmentsComponent
  }
];
