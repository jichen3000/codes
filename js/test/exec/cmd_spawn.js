//var spawn = require('child_process').spawn;
//var cmdProcess  = spawn('ls | grep js');
//var cmdProcess  = spawn('ls',['-l','-t']);
//var cmdProcess  = spawn('./echo.sh');
var exec=require('child_process').exec;
var cmdProcess = exec('ls |grep js');
//var stdin = process.openStdin();
process.stdin.resume();
process.stdin.pipe(cmdProcess.stdin);
/*
process.stdin.on('data', function(data){
  console.log('precess stdin on data: \n' + data);
  //cmdProcess.stdin.write(data);
  cmdProcess.stdin.write(data);
});
*/
process.stdin.on('exit', function (code, signal) {
    console.log('stdin exit code: %s', code);
});


cmdProcess.stdout.on('data', function (data) {
  console.log('cmd process stdout on data: \n %s', data);
});

cmdProcess.stderr.on('data', function (data) {
  console.log('cmd process stderr on data: \n %s', data);
});


cmdProcess.on('exit', function (code, signal) {
  console.log('cmd process on exit, code: %s', code);
    process.stdin.destroy();
});
