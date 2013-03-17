tty = require('tty');
util = require('util');
process.stdin.resume();
tty.setRawMode(true);
process.stdin.on('keypress', function(char, key){
  if(key && key.ctrl && key.name == 'c'){
    console.log('graceful exit');
    process.exit();
  }else{
    console.log('char: %s', char);
    console.log('key: %s', util.inspect(key));
  }
});