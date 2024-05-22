import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { User } from '../../models/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  getUserAuthToken(): Observable<boolean> {
    if (typeof localStorage !== 'undefined') {
      const token = localStorage.getItem('user_token');
      const role = localStorage.getItem('role');
      if (token && role === 'user') {
        return of(true);
      }
    }
    return of(false);
  }

  getDoctorAuthToken(): Observable<boolean> {
    if (typeof localStorage !== 'undefined') {
      const token = localStorage.getItem('doctor_token');
      const role = localStorage.getItem('role');
      if (token && role === 'doctor') {
        return of(true);
      }
    }
    return of(false);
  }
  getUserIdFromLocalStorage(): number {
    const userJson = localStorage.getItem('loggedUser');
    if (userJson) {
      const user: User = JSON.parse(userJson);
      return user.id;
    }
    return 0;
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('loggedUser');
  }

}
