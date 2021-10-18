const appendToEachArrayValue = (array, appendString) => {
  const newArr = [];
  for (const element of array) {
    newArr.push(`${appendString}${element}`);
  }

  return array;
};

export default appendToEachArrayValue;
