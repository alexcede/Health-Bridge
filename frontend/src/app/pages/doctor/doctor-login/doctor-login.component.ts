import { Component, inject } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { DoctorService } from '../../../core/services/doctor/doctor.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Router, RouterOutlet } from '@angular/router';
import { AuthService } from '../../../core/services/auth/auth.service';

@Component({
  selector: 'app-doctor-login',
  standalone: true,
  imports: [ButtonModule, InputTextModule, ReactiveFormsModule, CommonModule, HttpClientModule, RouterOutlet],
  templateUrl: './doctor-login.component.html',
  styleUrl: './doctor-login.component.css'
})
export class DoctorLoginComponent {
  form: FormGroup;
  errorMessage: string | null = null;
  constructor(private fb: FormBuilder, private doctorService: DoctorService, private router: Router, private authService: AuthService) {
    this.form = this.fb.group({
      email: ['', [Validators.required, Validators.email, Validators.pattern(/^\S+@\S+\.\S+$/)]],
      password: ['', [Validators.required, Validators.pattern(/^\S*$/)]]
    });
  }

  onSubmit() {
    this.errorMessage = null;
    if (this.form.valid) {
      this.doctorService.login(this.form.value).subscribe({
        next: (response) => {
          console.log(response);
          if (response.success) {
            // Save user data to localStorage
            localStorage.setItem('loggedUser', JSON.stringify(response.user));
            localStorage.setItem('doctor_token', response.token);
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
