import { DoctorAssignmentResponse, DoctorTableAssignmentResponse } from "./assignment";
import { userResponse } from "./user";

export interface Action<T = any> {
  action: string; // edit - delete
  row?: T // register
}

export const getEntityProperties = (entity: string): Array<any> => {

  let results: any = [];
  let resultClass: any;

  switch(entity) {
    case 'user':
      resultClass = new userResponse(); break;
    case 'doctorAssignment':
      resultClass = new DoctorTableAssignmentResponse; break;
  }

  if(resultClass){
    results = Object.keys(resultClass);
  }

  return results;
}
