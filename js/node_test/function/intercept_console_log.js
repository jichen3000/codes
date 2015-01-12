var msgCache = [];

function getMsgs (isClean) {
  isClean = typeof isClean !== 'undefined' ? isClean : true;
  var msgArr = msgCache.slice(0);
  if (isClean) msgCache.length = 0;
  return msgArr;
}



(function(){
  var oldLog = console.log;
  console.log = function (msg) {
    msgCache.push(msg);
    oldLog.apply(console, arguments);
  }
})();

if (require.main === module){
  require('testhelper');
  var assert = require('assert');

  console.log("123");
  console.log("456");
  console.log("mm");


  var msgs = getMsgs();
  assert(msgs.toString(), "123,456,mm");
  msgs = getMsgs();
  assert(msgs, []);

  console.log("mm");
  msgs = getMsgs();
  assert(msgs.toString(), "mm");

  "ok".p();
}
