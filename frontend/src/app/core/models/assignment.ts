export interface DoctorAssignment {
  id: number;
  email: string;
  password: string;
  dni: string;
  photo: string;
  name: string;
  firstSurname: string;
  secondSurname: string;
  phoneNumber: string;
  active: boolean;
}

export interface UserAssignment {
  id: number;
  email: string;
  password: string;
  photo: string;
  name: string;
  firstSurname: string;
  secondSurname: string;
  phoneNumber: string;
  healthCardCode: string;
  birthDate: string;
  gender: string;
  dni: string;
  address: string;
  postalCode: string;
  active: boolean;
}

export interface AssignmentResult {
  id: number;
  doctor: DoctorAssignment | number;
  user: UserAssignment | number;
  dateCreated: string;
}
