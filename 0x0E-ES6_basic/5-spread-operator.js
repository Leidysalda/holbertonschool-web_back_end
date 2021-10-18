const concatArrays = (array1, array2, string) => {
  const arr = [];
  arr.push(...array1, ...array2, ...string);
  return arr;
};

export default concatArrays;
