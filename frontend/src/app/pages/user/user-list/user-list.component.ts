import { Component, OnInit } from '@angular/core';
import { AsyncPipe } from '@angular/common';
import { UserItemComponent } from '../user-item/user-item.component';
import { ErrorMessageComponent } from '../../../shared/components/error-message/error-message.component'
import { UserService } from '../../../core/services/user/user.service';
import { catchError, Observable, EMPTY } from 'rxjs';
import { User } from '../../../core/models/user';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [AsyncPipe, UserItemComponent, ErrorMessageComponent],
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {
  public userList$!: Observable<User[]>;
  public errorMessage!: string;
  constructor(private service: UserService) {}

  ngOnInit(): void {
    this.userList$ = this.service.getUsers().pipe(catchError
      ((error:string) => {
        this.errorMessage = error;
        return EMPTY;
    }));
  }

  trackById(index: number, item: User): number {
    return item.id;
  }
}
