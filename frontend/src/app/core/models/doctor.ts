export interface Doctor {
  id:number,
  email:string,
  password:string,
  dni:string,
  photo:string,
  name:string,
  firstSurname:string,
  secondSurname:string,
  phoneNumber:number,
  active:boolean
}

export class Doctor {
  id: number = 0;
  email: string = '';
  password: string = '';
  dni: string = '';
  photo: string = '';
  name: string = '';
  firstSurname: string = '';
  secondSurname: string = '';
  phoneNumber: number = 0;
  active: boolean = false;
}
