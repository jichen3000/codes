require("testhelper")

function exitHandler(options, err) {
  if (options.cleanup) console.log('clean');
  if (err) {
    console.log('in error')
    console.log(err.stack);
  }
  if (options.exit) {console.log('at SIGINT'); process.exit()};
}

function onOnce(obj, event_name, func){
  // event_name.pp()
  // obj.p()
  if (typeof obj._events[event_name]==="undefined"){
    obj.on(event_name, func);
    return obj;
  }
  if (obj._events[event_name].length === 1){
    if(obj._events[event_name] === func){
      return obj;
    }
  } else {
    for (var index = 0; index<obj._events[event_name].length; index++) {
      if (func === obj._events[event_name][index]) {
        return obj;
      }
    }
  }
  obj.on(event_name, func);
  return obj;
}

//do something when app is closing
// process.on('exit', exitHandler.bind(null,{cleanup:true}));
// process.on('exit', exitHandler.bind(null,{cleanup:true}));
var newExit = exitHandler.bind(null,{cleanup:true});
onOnce(process, 'exit', newExit);
onOnce(process, 'exit', newExit);
onOnce(process, 'exit', newExit);

process._events.pp()

//catches ctrl+c event
// process.stdin.resume();
// process.on('SIGINT', exitHandler.bind(null, {exit:true}));

//catches uncaught exceptions
// process.on('uncaughtException', exitHandler.bind(null, {exit:true}));

// aa.p()