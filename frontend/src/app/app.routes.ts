import { Routes } from '@angular/router';
import { userGuard } from './core/guards/userGuard/user-guard.guard';
import { LoginComponent } from './pages/user/login/login.component';
import { DoctorLoginComponent } from './pages/doctor/doctor-login/doctor-login.component';
import { DOCTOR_ROUTES } from './pages/doctor/doctor.routes';
import { doctorGuard } from './core/guards/doctorGuard/doctor-guard.guard';

export const routes: Routes = [
  {
    path:'',
    loadChildren: () => import('./pages/index/index.routes').then(m => m.INDEX_ROUTES)
  },
  {
    path:'admin',
    loadChildren: () => import('./pages/admin/admin.routes').then(m => m.ADMIN_ROUTES)
  },
  {
    path: 'doctor',
    canMatch: [doctorGuard],
    loadChildren: () => import('./pages/doctor/doctor.routes').then(m => m.DOCTOR_ROUTES)
  },
  {
    path: 'user',
    canMatch: [userGuard],
    loadChildren: () => import('./pages/user/user.routes').then(m => m.USER_ROUTES)
  },
  {
    path: 'user/login',
    component: LoginComponent,
  },
  {
    path: 'doctor/login',
    component: DoctorLoginComponent
  },
  {
    path: '**',
    loadComponent: () => import('./shared/components/not-found/not-found.component').then(comp => comp.NotFoundComponent)
  }
];
