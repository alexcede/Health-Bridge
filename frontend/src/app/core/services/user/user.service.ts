import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, firstValueFrom, map, Observable, throwError } from 'rxjs';
import { User } from '../../models/user'
import { environment } from '../../../../environments/environment.development';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  private userApiUrl = `${environment.apiUrlBase}user/`;
  constructor(private http: HttpClient) { }

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.userApiUrl);
  }

  login(formValue: any): Observable<any> {
    return this.http.post<any>(this.userApiUrl + 'login/', formValue);
  }

  getUser(id: number): Observable<User> {
    return this.http.get<User>(this.userApiUrl + id + '/').pipe(
      map((user: User) => user)
    )
  }
  activateUser(id: number): Observable<any> {
    return this.http.get(this.userApiUrl + `activate/${id}/`)
  }
  deleteUser(id: number): Observable<any> {
    return this.http.delete(this.userApiUrl + `delete/${id}/`);
  }

  getUserRecipes(userId: number): Observable<any> {
    return this.http.get(this.userApiUrl + `recipes/${userId}/`);
  }
}
