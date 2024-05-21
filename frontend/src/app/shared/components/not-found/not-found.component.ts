import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [],
  templateUrl: './not-found.component.html',
  styleUrl: './not-found.component.css'
})
export class NotFoundComponent implements OnInit{
  constructor(private router:Router) { }

  ngOnInit(): void {

  }
  redirectToHome() {
    this.router.navigate(['/']);
  }
}
