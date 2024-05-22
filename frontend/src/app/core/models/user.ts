export interface User {
  id: number;
  email: string;
  password: string;
  photo: string;
  name: string;
  firstSurname: string;
  secondSurname: string;
  phoneNumber: number;
  healthCardCode: number;
  birthDate: Date;
  gender: string;
  dni: string;
  address: string;
  postalCode: number;
  active: boolean;
}

export class userResponse {
  id = 0
  email = ''
  password = ''
  photo = ''
  name = ''
  firstSurname = ''
  secondSurname = ''
  phoneNumber = 0
  healthCardCode = 0
  birthDate = Date
  gender = ''
  dni = ''
  address = ''
  postalCode = 0
  active = Boolean
}
