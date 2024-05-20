export interface Report {
  id: number,
  reportName: string,
  disease: string,
  reportInfo: string,
  dateCreated: Date,
  doctor_id: number,
  user_id: number
}
