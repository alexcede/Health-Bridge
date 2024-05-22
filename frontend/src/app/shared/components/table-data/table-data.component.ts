import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Action } from '../../../core/models/table-column';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ModelPopupComponent } from '../model-popup/model-popup.component';
@Component({
  selector: 'app-table-data',
  standalone: true,
  imports: [CommonModule, FormsModule, ModelPopupComponent],
  templateUrl: './table-data.component.html',
  styleUrls: ['./table-data.component.css']
})
export class TableDataComponent {

  constructor() {}

  title = '';
  columns: string[] = [];
  originalDataSource: any = []; // Copia separada de los datos originales
  filterDataSource: any = [];
  dataSource: any = [];
  isActive: boolean = false;
  isDataUpdated: boolean = false; // Variable para indicar si los datos se han actualizado

  filters: {
    name: string;
    firstSurname: string,
    secondSurname: string,
    phoneNumber: string;
    dni: string;
    active: boolean | null;
    email: string;
  } = {
    name: '',
    firstSurname: '',
    secondSurname: '',
    phoneNumber: '',
    dni: '',
    active: null,
    email: ''
  };

  trackByIndex(index: number, item: any): any {
    return index;
  }

  @Input() set tableTitle(title: string) {
    this.title = title;
  }

  @Input() set tableColumns(columns: string[]) {
    this.columns = columns;
  }

  @Input() set tableData(data: any) {
    this.originalDataSource = data;
    this.filterDataSource = data;
    this.dataSource = data;
    this.isDataUpdated = true;
  }

  @Output() tableAction: EventEmitter<Action> = new EventEmitter();

  onAction(tableAction: string, row?: any) {
    this.tableAction.emit({ action: tableAction, row: row });
  }

  toggleActiveFilter() {
    // Restaurar los datos filtrados a los originales
    this.dataSource = this.originalDataSource.slice();

    if (this.filters.active !== null) {
      // Filtrar los datos según el estado activo
      this.dataSource = this.dataSource.filter((item: any) => item.active === this.filters.active);
    }
    // Marcar que los datos se han actualizado
    this.isDataUpdated = true;
  }

  filteredData() {
    let filtered = this.dataSource.filter((item: any) => {
      const matchesName = !this.filters.name || (item.hasOwnProperty('name') && item.name.toLowerCase().includes(this.filters.name.toLowerCase()));
      const matchesFirstSurname = !this.filters.firstSurname || (item.hasOwnProperty('firstSurname') && item.firstSurname.toLowerCase().includes(this.filters.firstSurname.toLowerCase()));
      const matchesSecondSurname = !this.filters.secondSurname || (item.hasOwnProperty('secondSurname') && item.secondSurname.toLowerCase().includes(this.filters.secondSurname.toLowerCase()));
      const matchesPhone = !this.filters.phoneNumber || (item.hasOwnProperty('phoneNumber') && item.phoneNumber.toString().includes(this.filters.phoneNumber));
      const matchesDni = !this.filters.dni || (item.hasOwnProperty('dni') && item.dni.toLowerCase().includes(this.filters.dni.toLowerCase()));
      return matchesName && matchesPhone && matchesDni && matchesFirstSurname && matchesSecondSurname;
    });

    if (this.filters.active !== null) {
      filtered = filtered.filter((item: any) => item.active === this.filters.active);
    }

    return filtered;
  }
}
