#!/usr/bin/node
const createReportObject = (employeesList) => {
  const allEmployees = employeesList;
  const getNumberOfDepartments = (obj) => Object.keys(obj).length;
  return { allEmployees, getNumberOfDepartments };
};

export default createReportObject;
