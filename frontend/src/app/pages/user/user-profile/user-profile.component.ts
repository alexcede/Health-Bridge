import { Component, OnDestroy, OnInit } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { map, Observable, Subscription, switchMap } from 'rxjs';
import { User } from '../../../core/models/user';
import { ActivatedRoute, Router, RouterOutlet } from '@angular/router';
import { UserService } from '../../../core/services/user/user.service';
import { CommonModule } from '@angular/common';
import { MatCardAvatar, MatCardContent, MatCardHeader, MatCardImage, MatCardModule } from '@angular/material/card';
import { TableDataComponent } from '../../../shared/components/table-data/table-data.component';
import { MatDialog } from '@angular/material/dialog';
import { AuthService } from '../../../core/services/auth/auth.service';
import { Action } from '../../../core/models/table-column';
import { ReportDetailDialogComponent } from '../../report/report-detail-dialog/report-detail-dialog.component';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [HeaderComponent, CommonModule, MatCardModule, RouterOutlet, MatCardAvatar, MatCardContent,MatCardHeader,MatCardImage, TableDataComponent],
  templateUrl: './user-profile.component.html',
  styleUrl: './user-profile.component.css'
})
export class UserProfileComponent implements OnInit, OnDestroy {
  public userId: number = 0;
  user: User | undefined;
  private sub: Subscription = new Subscription();

  constructor(
    private activatedRoute: ActivatedRoute,
    private userService: UserService,
    private router: Router,
    private authService: AuthService,
    private dialog: MatDialog,
  ) { }
  public recipes: any[] = [];
  public columns: string[] = [];
  public title: string = 'your recipes';

  ngOnInit(): void {
    this.sub = this.activatedRoute.params.subscribe(params => {
      this.userId = params['id'];
      this.userService.getUser(this.userId).subscribe(user => {
        this.user = user;
      });
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

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }
}
