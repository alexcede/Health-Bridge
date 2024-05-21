import { CanActivateFn, CanMatchFn} from '@angular/router';
import { AuthService } from '../../services/auth/auth.service';
import { inject } from '@angular/core';

export const userGuard: CanMatchFn = (route, state) => {
  const authService = inject(AuthService);
  return authService.getUserAuthToken();
};
