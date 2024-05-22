import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-doctor-header',
  standalone: true,
  imports: [RouterLink, RouterOutlet, CommonModule],
  templateUrl: './doctor-header.component.html',
  styleUrl: './doctor-header.component.css'
})
export class DoctorHeaderComponent implements OnInit{
  menuValue:boolean = false;
  menu_icon:string = 'bi bi-list';
  loggedIn: boolean = false;
  doctorId: number = 0;

  constructor(private router: Router) { }
  ngOnInit(): void {
    
  }
  openMenu(){
    this.menuValue =! this.menuValue;
    this.menu_icon = this.menuValue ? 'bi bi-x' : 'bi bi-list';
  }

  closeMenu() {
    this.menuValue = false;
    this.menu_icon = 'bi bi-list';
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
