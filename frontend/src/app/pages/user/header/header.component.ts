import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, RouterOutlet, CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{
  menuValue:boolean = false;
  menu_icon:string = 'bi bi-list';
  loggedIn: boolean = false;
  userId: number = 0;
  constructor(private router: Router) { }
  ngOnInit(): void {
      this.checkUser();
  }
  openMenu(){
    this.menuValue =! this.menuValue;
    this.menu_icon = this.menuValue ? 'bi bi-x' : 'bi bi-list';
  }

  closeMenu() {
    this.menuValue = false;
    this.menu_icon = 'bi bi-list';
  }
  checkUser(): void {
    if (typeof window !== 'undefined') {
      const userString = localStorage.getItem('loggedUser');
      if(userString && localStorage.getItem('user_token')) {
        const user = JSON.parse(userString);
        this.userId = user.id;
        this.loggedIn = true;
      } else {
        this.loggedIn = false;
      }
    }
  }
  logout(): void {
    if (typeof window !== 'undefined' && window.localStorage) {
      this.router.navigateByUrl('/').then(() => {
        window.localStorage.clear();
        setTimeout(() => {
          window.location.reload();
        }, 10);
      });
    }
  }
}
