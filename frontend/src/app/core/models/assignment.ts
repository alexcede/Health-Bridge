export interface DoctorAssignmentResult {
  id: number;
  doctor: number;
  user: number;
  dateCreated: string;
  active: boolean;
}
export interface DoctorTableAssignmentResult {
  id: number;
  doctor: string;
  doctor_name: string;
  user: string;
  user_name: string;
  dateCreated: string;
  active: boolean;
}

export class DoctorTableAssignmentResponse {
  id = 0;
  doctor = '';
  doctor_name = '';
  user = '';
  user_name = '';
  dateCreated = '';
  active = true;
}

export class DoctorAssignmentResponse {
  id = 0;
  doctor = 0;
  user = 0;
  dateCreated = '';
  active = Boolean;
}


