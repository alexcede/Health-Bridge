import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment.development';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AssignmentService {

  private assignmentApiUrl = `${environment.apiUrlBase}assignment/`;
  constructor(private http: HttpClient) { }

  activateAssignment(id: number): Observable<any> {
    return this.http.get(this.assignmentApiUrl + `activate/${id}/`)
  }

  deactivateAssignment(id: number): Observable<any> {
    return this.http.delete(this.assignmentApiUrl + `delete/${id}/`)
  }
}
