import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DialogCustomData } from '../../models/model-content';
import { ModelPopupComponent } from '../../../shared/components/model-popup/model-popup.component';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DialogService {
  
  private isOpenSubject = new BehaviorSubject<boolean>(false);
  isOpen$ = this.isOpenSubject.asObservable();

  openPopup() {
    this.isOpenSubject.next(true);
  }

  closePopup() {
    this.isOpenSubject.next(false);
  }
}
