import { Component, OnInit } from '@angular/core';
import { AsyncPipe } from '@angular/common';
import { ErrorMessageComponent } from '../../../shared/components/error-message/error-message.component'
import { UserService } from '../../../core/services/user/user.service';
import { User } from '../../../core/models/user';
import { Action, getEntityProperties } from '../../../core/models/table-column';
import { TableDataComponent } from '../../../shared/components/table-data/table-data.component';
import { ModelPopupComponent } from '../../../shared/components/model-popup/model-popup.component';
import { MatDialog } from '@angular/material/dialog';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [AsyncPipe, ErrorMessageComponent, TableDataComponent, ReactiveFormsModule],
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {
  constructor(private service: UserService, private dialog: MatDialog) { }

  public userList: User[] = [];
  public errorMessage!: string;

  public columns: string[] = []
  title:string = 'users';

  ngOnInit(): void {

    this.columns = getEntityProperties('user')

    this.loadUsers()
  }

  loadUsers() {
    this.service.getUsers().subscribe(data => {
      this.userList = data;
    });
  }

  onAction(tableAction: Action) {
    if(tableAction.action == 'Edit') {
      this.edit(tableAction.row)
    } else if(tableAction.action == 'Delete') {
      this.delete(tableAction.row.id);
    } else if(tableAction.action == 'Activate') {
      this.activate(tableAction.row.id)
    }
  }

  confirmDelete(user: User) {
    const dialogRef = this.dialog.open(ModelPopupComponent, {
      data: {
        content: user.name,
        firstSurname: user.firstSurname,
        secondSurname: user.secondSurname
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.onAction({ action: 'Delete', row: user });
      }
    });
  }

  delete(userId: number) {
    this.service.deleteUser(userId).subscribe(
      response => {
        console.log(response);
        // Actualizar la lista después de la eliminación
        this.loadUsers();
      },
      error => {
        console.error('Error deleting user:', error);
      }
    );
  }
  edit(object: any){
    console.log(object)
  }
  activate(userId: number) {
    this.service.activateUser(userId).subscribe(
      response => {
        console.log(response);

        this.loadUsers();
      },
      error => {
        console.error('Error updating user:', error);
      }
    );
  }


  trackById(index: number, item: User): number {
    return item.id;
  }
}
