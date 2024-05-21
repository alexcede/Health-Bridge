import { Component, OnDestroy, OnInit } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { map, Observable, Subscription, switchMap } from 'rxjs';
import { User } from '../../../core/models/user';
import { ActivatedRoute, RouterOutlet } from '@angular/router';
import { UserService } from '../../../core/services/user/user.service';
import { CommonModule } from '@angular/common';
import { MatCardAvatar, MatCardContent, MatCardHeader, MatCardImage, MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [HeaderComponent, CommonModule, MatCardModule, RouterOutlet, MatCardAvatar, MatCardContent,MatCardHeader,MatCardImage],
  templateUrl: './user-profile.component.html',
  styleUrl: './user-profile.component.css'
})
export class UserProfileComponent implements OnInit, OnDestroy {
  public userId: number = 0;
  public user: User | null = null;
  private sub: Subscription = new Subscription();

  constructor(
    private activatedRoute: ActivatedRoute,
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.sub = this.activatedRoute.params.subscribe(params => {
      this.userId = params['id'];
      this.userService.getUser(this.userId).subscribe(user => {
        this.user = user;
      });
    });
  }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }
}
