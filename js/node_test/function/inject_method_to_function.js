function test () {
  console.log("in "+this);
}

function test1 () {
  console.log(this);
}

Object.defineProperty( Object.prototype, "test", {
    value: test, enumerable: false});

if (require.main === module) {
  require('testhelper');
  
  test.pp();
  (typeof test).pp();
  (test === test1).pp();

  test1.test();

  "ok".p();
}