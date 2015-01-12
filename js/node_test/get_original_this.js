var mustEqual = function (expectedValue) {
  console.log("typeof this: "+(typeof this));
  console.log("typeof expectedValue: "+(typeof expectedValue));
  console.log("is equal: "+(this === expectedValue));
}

Object.defineProperty( Object.prototype, "mustEqual", {
    value: mustEqual, enumerable: false});
Object.defineProperty( Number.prototype, "mustEqual", {
    value: mustEqual, enumerable: false});


if (require.main === module) {
  (1).mustEqual(1);
  ('str').mustEqual('str');
}