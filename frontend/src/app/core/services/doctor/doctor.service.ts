import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from './../../../../environments/environment.development';
import { map, Observable } from 'rxjs';
import { Doctor } from '../../models/doctor';
import { DoctorAssignmentResult } from '../../models/assignment';
@Injectable({
  providedIn: 'root'
})
export class DoctorService {

  private doctorApiUrl = `${environment.apiUrlBase}doctor/`;
  constructor(private http: HttpClient) { }

  login(formValue: any): Observable<any> {
    return this.http.post<any>(this.doctorApiUrl + 'login/', formValue);
  }

  getDoctorAssignments(id: number): Observable<DoctorAssignmentResult[]> {
    return this.http.get<DoctorAssignmentResult[]>(this.doctorApiUrl + `assignment/${id}/`)
  }

  getDoctor(id: number): Observable<Doctor> {
    return this.http.get<Doctor>(this.doctorApiUrl + id + '/').pipe(
      map((doctor: Doctor) => doctor)
    )
  }
}
