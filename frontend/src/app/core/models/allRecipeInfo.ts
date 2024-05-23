export interface Recipe {
  id: number;
  doctor: string;
  reportName: string;
  dateCreated: string;
  dateFinish: string;
  medicines: Medicine[];
}

export interface Medicine {
  name: string;
  morning_dose: number;
  noon_dose: number;
  night_dose: number;
}
