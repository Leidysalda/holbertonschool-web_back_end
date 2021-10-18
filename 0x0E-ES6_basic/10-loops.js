const appendToEachArrayValue = (array, appendString) => {
  const newArr = [];
  for (const element of array) {
    newArr.push(`${appendString}${element}`);
  }
  return newAr;
};

export default appendToEachArrayValue;
