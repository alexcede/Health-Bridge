import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment.development';
import { Observable, tap, catchError, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {

  private recipeApiUrl = `${environment.apiUrlBase}recipe/`;
  constructor(private http: HttpClient) { }

  createReport(reportData: any): Observable<any> {
    return this.http.post(`${this.recipeApiUrl}/reports/`, reportData).pipe(
      tap((newReport: any) => console.log(`Added report w/ id=${newReport.id}`)),
      catchError(this.handleError<any>('createReport'))
    );
  }

  getAllMedicines(): Observable<any> {
    return this.http.get(`${this.recipeApiUrl}/reports/`).pipe(
      tap((newReport: any) => console.log(`Added report w/ id=${newReport.id}`)),
      catchError(this.handleError<any>('createReport'))
    );
  }

  createRecipe(recipeData: any): Observable<any> {
    return this.http.post(`${this.recipeApiUrl}/recipes/`, recipeData).pipe(
      tap((newRecipe: any) => console.log(`Added recipe w/ id=${newRecipe.id}`)),
      catchError(this.handleError<any>('createRecipe'))
    );
  }

  createRecipeInfo(recipeInfoData: any): Observable<any> {
    return this.http.post(`${this.recipeApiUrl}/recipeInfos/`, recipeInfoData).pipe(
      tap((newRecipeInfo: any) => console.log(`Added recipe info w/ id=${newRecipeInfo.id}`)),
      catchError(this.handleError<any>('createRecipeInfo'))
    );
  }

  createMedicine(medicineData: any): Observable<any> {
    return this.http.post(`${this.recipeApiUrl}/medicines/`, medicineData).pipe(
      tap((newMedicine: any) => console.log(`Added medicine w/ id=${newMedicine.id}`)),
      catchError(this.handleError<any>('createMedicine'))
    );
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}
