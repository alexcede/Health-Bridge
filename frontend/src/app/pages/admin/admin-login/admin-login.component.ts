import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterOutlet } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { HeaderComponent } from '../../user/header/header.component';
import { AuthService } from '../../../core/services/auth/auth.service';
import { DoctorService } from '../../../core/services/doctor/doctor.service';
import { AdminService } from '../../../core/services/admin/admin.service';

@Component({
  selector: 'app-admin-login',
  standalone: true,
  imports: [ButtonModule, InputTextModule,HeaderComponent, ReactiveFormsModule, CommonModule, HttpClientModule, RouterOutlet],
  templateUrl: './admin-login.component.html',
  styleUrl: './admin-login.component.css'
})
export class AdminLoginComponent {
  form: FormGroup;
  errorMessage: string | null = null;
  constructor(private fb: FormBuilder, private adminService: AdminService, private router: Router, private authService: AuthService) {
    this.form = this.fb.group({
      email: ['', [Validators.required, Validators.email, Validators.pattern(/^\S+@\S+\.\S+$/)]],
      password: ['', [Validators.required, Validators.pattern(/^\S*$/)]]
    });
  }

  onSubmit() {
    this.errorMessage = null;
    if (this.form.valid) {
      this.adminService.login(this.form.value).subscribe({
        next: (response) => {
          console.log(response);
          if (response.success) {
            // Save user data to localStorage
            localStorage.setItem('loggedUser', JSON.stringify(response.user));
            localStorage.setItem('admin_token', response.token);
            localStorage.setItem('role', response.role);
            console.log(localStorage.getItem('loggedUser'))
            this.router.navigate(['doctor/dashboard']);
          } else {
            this.errorMessage = 'Incorrect credentials, please try again.';
          }
        },
        error: () => {
          this.errorMessage = 'Incorrect credentials, please try again.';
        }
      });
    } else {
      this.errorMessage = 'Please fill out all required fields correctly.';
    }
  }

  get email() {
    return this.form.get('email');
  }

  get password() {
    return this.form.get('password');
  }
}
