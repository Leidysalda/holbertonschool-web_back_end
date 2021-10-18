const appendToEachArrayValue = (array, appendString) => {
  const newArr = [];
  for (const element of array) {
    newArr.push(`${appendString}${element}`);
  }
  return newArr;
};

export default appendToEachArrayValue;
