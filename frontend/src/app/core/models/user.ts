export interface User {
  id: number;
  email: string;
  password: string;
  photo: string;
  name: string;
  firstSurname: string;
  secondSurname: string;
  phoneNumber: number;
  healthBarCode: number;
  birthdate: Date;
  gender: string;
  dni: string;
  address: string;
  postalCode: number;
  active: boolean;
}
