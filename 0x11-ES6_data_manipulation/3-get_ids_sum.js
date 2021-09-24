export default function getStudentIdsSum(getListStudents) {
  if (Array.isArray(getListStudents)) {
    return getListStudents.reduce((accumulador, current) => accumulador + current.id, 0);
  }
  return [];
}