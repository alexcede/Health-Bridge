import { User } from './../../../core/models/user';
import { Component, inject } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { HeaderComponent } from '../header/header.component';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { UserService } from '../../../core/services/user/user.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Router, RouterOutlet } from '@angular/router';
import { AuthService } from '../../../core/services/auth/auth.service';
import { UserFooterComponent } from '../user-footer/user-footer.component';
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ButtonModule, InputTextModule,HeaderComponent, ReactiveFormsModule, CommonModule, HttpClientModule, RouterOutlet, UserFooterComponent],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  form: FormGroup;
  errorMessage: string | null = null;
  constructor(private fb: FormBuilder, private userService: UserService, private router: Router, private authService: AuthService) {
    this.form = this.fb.group({
      email: ['', [Validators.required, Validators.email, Validators.pattern(/^\S+@\S+\.\S+$/)]],
      password: ['', [Validators.required, Validators.pattern(/^\S*$/)]]
    });
  }

  onSubmit() {
    this.errorMessage = null;
    if (this.form.valid) {
      this.userService.login(this.form.value).subscribe({
        next: (response) => {
          console.log(response);
          if (response.success) {
            // Save user data to localStorage
            localStorage.setItem('loggedUser', JSON.stringify(response.user));
            localStorage.setItem('user_token', response.token);
            localStorage.setItem('role', response.role);

            this.router.navigate(['/user', response.user.id]);
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
