var util = require('util');

var puts = console.log;

function MyError(message){
  this.name = "MyError";
  this.message = message;
}

// MyError.prototype = new Error();
// MyError.prototype.constructor = MyError;

util.inherits(MyError, Error);

if (require.main === module) {
  require('testhelper');
  try {
    throw new MyError("it is my error.");
  } catch (err) {
    err.p();
    err.message.p();
    err.name.p();
    err.super_.stack.p();
  }

  // notice: cannot catch special error
  try {
    throw new MyError("it is my error.");
  } catch (err) {
    if (err instanceof Error){
      err.message.p();
      err.stack.p();
    } else {
      throw err;
    }
  }
  "ok".p();
}