var puts = console.log;

function something (arg1, arg2) {
  if(typeof arg1 === 'undefined'){
    throw new Error("need at least an argument!");
  }
}

if (require.main === module) {
  require('testhelper');
  try {
    something();
  } catch (err) {
    err.p();
    err.message.p();
    err.name.p();
    err.stack.p();
  }

  // notice: cannot catch special error
  try {
    aa.bb();
  } catch (err) {
    if (err instanceof ReferenceError){
      err.message.p();
      err.stack.p();
    } else {
      throw err;
    }
  }
  "ok".p();
}