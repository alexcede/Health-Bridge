import { DoctorHeaderComponent } from '../doctor-header/doctor-header.component';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterOutlet } from '@angular/router';
import { UserService } from '../../../core/services/user/user.service';
import { User } from '../../../core/models/user';
import { CommonModule } from '@angular/common';
import { MatCardModule, MatCardAvatar, MatCardContent, MatCardHeader, MatCardImage } from '@angular/material/card';
@Component({
  selector: 'app-doctor-user-profile',
  standalone: true,
  imports: [DoctorHeaderComponent, CommonModule, MatCardModule, RouterOutlet, MatCardAvatar, MatCardContent,MatCardHeader,MatCardImage],
  templateUrl: './doctor-user-profile.component.html',
  styleUrl: './doctor-user-profile.component.css'
})
export class DoctorUserProfileComponent implements OnInit{
  user: User | undefined;

  constructor(
    private route: ActivatedRoute,
    private userService: UserService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const userId = params['id'];
      if (userId) {
        this.userService.getUser(userId).subscribe(user => {
          this.user = user;
        });
      }
    });
  }
}
