// http://stackoverflow.com/questions/7486085/copying-array-by-value-in-javascript

var copyArray = function (originalArr) {
  return originalArr.slice(0);
}

var copyArray2 = function (originalArr) {
  var theArr = originalArr.slice(0)
  return theArr;
}

if (require.main === module) {
  require('testhelper');
  var assert = require('assert');
  originalArr = [1,2,3];
  copiedArr = copyArray(originalArr);
  assert.deepEqual(originalArr, copiedArr);
  copiedArr.push(4);
  assert.deepEqual(copiedArr, [1,2,3,4]);

  copiedArr2 = copyArray2(originalArr);
  assert.deepEqual(originalArr, copiedArr2);

  "ok".p();
}