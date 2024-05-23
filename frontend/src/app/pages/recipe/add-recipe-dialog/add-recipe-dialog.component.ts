import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { RecipeService } from '../../../core/services/recipe/recipe.service';
import { Report } from '../../../core/models/report';
import { Recipe } from '../../../core/models/recipe';
import { Medicine } from '../../../core/models/medicine';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-add-recipe-dialog',
  templateUrl: './add-recipe-dialog.component.html',
  imports: [CommonModule, ReactiveFormsModule],
  standalone: true,
  styleUrls: ['./add-recipe-dialog.component.css']
})
export class AddRecipeDialogComponent implements OnInit {
  medicines: Medicine[] = [];
  currentStep = 1;

  constructor(
    public reportForm: FormGroup,
    public recipeForm: FormGroup,
    private fb: FormBuilder,
    private recipeService: RecipeService,
  ) { }

  ngOnInit(): void {
    this.initializeForms();
    this.loadMedicines();
  }
  // Funciones para navegar entre pasos
  nextStep() {
    this.currentStep++;
  }

  previousStep() {
    this.currentStep--;
  }
  onSubmit() {
    // Lógica para enviar el formulario dependiendo del paso actual
    if (this.currentStep === 4) {
      // Envío final de la receta
    }
  }
  
  initializeForms(): void {
    this.reportForm = this.fb.group({
      reportName: ['', Validators.required],
      disease: ['', Validators.required],
      reportInfo: ['', Validators.required]
    });

    this.recipeForm = this.fb.group({
      dateFinish: ['', Validators.required],
      morningDose: ['0', Validators.required],
      noonDose: ['0', Validators.required],
      nightDose: ['0', Validators.required]
    });
  }

  loadMedicines(): void {
    this.recipeService.getAllMedicines().subscribe(
      (data) => {
        this.medicines = data;
      },
      (error) => {
        console.error('Error fetching medicines:', error);
      }
    );
  }


}
