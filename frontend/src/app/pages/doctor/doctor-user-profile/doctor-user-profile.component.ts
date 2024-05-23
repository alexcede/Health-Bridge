import { DoctorHeaderComponent } from '../doctor-header/doctor-header.component';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterOutlet } from '@angular/router';
import { UserService } from '../../../core/services/user/user.service';
import { User } from '../../../core/models/user';
import { CommonModule } from '@angular/common';
import { MatCardModule, MatCardAvatar, MatCardContent, MatCardHeader, MatCardImage } from '@angular/material/card';
import { Action } from '../../../core/models/table-column';
import { AuthService } from '../../../core/services/auth/auth.service';
import { TableDataComponent } from '../../../shared/components/table-data/table-data.component';
import { ReportDetailDialogComponent } from '../../report/report-detail-dialog/report-detail-dialog.component';
import { MatDialog } from '@angular/material/dialog';
import { AddRecipeDialogComponent } from '../../recipe/add-recipe-dialog/add-recipe-dialog.component';
import { ReactiveFormsModule } from '@angular/forms';
@Component({
  selector: 'app-doctor-user-profile',
  standalone: true,
  imports: [
    DoctorHeaderComponent,
    CommonModule,
    MatCardModule,
    RouterOutlet,
    MatCardAvatar,
    MatCardContent,
    MatCardHeader,
    MatCardImage,
    TableDataComponent,
  ],
  templateUrl: './doctor-user-profile.component.html',
  styleUrl: './doctor-user-profile.component.css'
})
export class DoctorUserProfileComponent implements OnInit{
  user: User | undefined;

  constructor(
    private activatedRoute: ActivatedRoute,
    private userService: UserService,
    private dialog: MatDialog,
  ) { }

  public recipes: any[] = [];
  public columns: string[] = [];
  public title: string = 'Recipes';
  public userId: number = 0;

  ngOnInit(): void {
    this.activatedRoute.params.subscribe(params => {
      this.userId = params['id'];
      if (this.userId) {
        this.userService.getUser(this.userId).subscribe(user => {
          this.user = user;
        });
      }
    });

    this.columns = ['report_name', 'disease', 'date_created', 'date_finish'];
    this.loadRecipes();
  }

  loadRecipes() {
    // Llama al servicio para obtener las recetas del usuario actual
    this.userService.getUserRecipes(this.userId).subscribe(
      (data) => {
        console.log(data)
        this.recipes = data.user_recipes;
      },
      (error) => {
        console.error('Error fetching user recipes:', error);
      }
    );
  }

  onAction(tableAction: Action) {
    if (tableAction.action === 'Info') {
      console.log(tableAction.row)
      const dialogRef = this.dialog.open(ReportDetailDialogComponent, {
        width: '1000px',
        data: tableAction.row
      });
    }
  }
  addNewRecipe(): void {

  }
}
