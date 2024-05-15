import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class BackendApiService {
  readonly APIUrl= "http://127.0.0.1:8000";
  readonly PhotoUrl = "http://127.0.0.1:8000/api/"

  constructor(private http: HttpClient) { }

  getUsers():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/user/');
  }
}
