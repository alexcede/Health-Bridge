import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from '../header/header.component';

@Component({
  selector: 'app-user-assignments',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent],
  templateUrl: './user-assignments.component.html',
  styleUrl: './user-assignments.component.css'
})
export class UserAssignmentsComponent {

}
