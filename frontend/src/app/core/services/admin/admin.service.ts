import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Admin } from '../../models/admin'
import { environment } from '../../../../environments/environment.development';
@Injectable({
  providedIn: 'root'
})
export class AdminService {

  private adminApiUrl = `${environment.apiUrlBase}admin/`;
  constructor(private http: HttpClient) { }

  login(formValue: any): Observable<any> {
    return this.http.post<any>(this.adminApiUrl + 'login/', formValue);
  }
}
