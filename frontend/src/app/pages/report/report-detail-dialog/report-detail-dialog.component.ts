import { CommonModule } from '@angular/common';
import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-report-detail-dialog',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './report-detail-dialog.component.html',
  styleUrl: './report-detail-dialog.component.css'
})
export class ReportDetailDialogComponent {

  constructor(@Inject(MAT_DIALOG_DATA) public report: any) { }
}
