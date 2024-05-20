import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  getAuthToken(): Observable<boolean>{
    return of(true);
  }

  login(userData: any): void {
    localStorage.setItem('currentUser', JSON.stringify(userData));
  }

  logout(): void {
    localStorage.removeItem('currentUser');
  }

  getCurrentUser(): any {
    return JSON.parse(localStorage.getItem('currentUser') || '{}');
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('currentUser');
  }
    
}
