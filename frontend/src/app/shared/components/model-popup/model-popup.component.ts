import { Component, Inject, Input } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef,MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { DialogCustomData } from '../../../core/models/model-content';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-model-popup',
  standalone: true,
  imports: [MatDialogModule, MatButtonModule, CommonModule],
  templateUrl: './model-popup.component.html',
  styleUrl: './model-popup.component.css'
})
export class ModelPopupComponent {
  @Input() title: string;
  @Input() message: string;
  @Input() buttonText: string;
  isOpen: boolean = false;

  constructor() {
    this.title = '';
    this.message = '',
    this.buttonText = '';
  }

  openPopup() {
    this.isOpen = true;
  }

  closePopup() {
    this.isOpen = false;
  }
}
