var exec=require('child_process').exec;
var cmdProcess = exec('ssh 72.46.131.199 -p 2222',
  function(error,stdout,stderr){
//var cmdProcess = exec('./echo.sh',function(error,stdout,stderr){
    //console.log("stdout: %s", stdout);
    //console.log("stderr: %s", stderr);
    if(error !== null){
	console.log("exec error: %s", error);
    }
});
process.stdin.resume();
process.stdin.pipe(cmdProcess.stdin);

process.stdin.on('data', function(data){
  console.log('precess stdin on data: \n' + data);
  //cmdProcess.stdin.write(data);
  //cmdProcess.stdin.write(data);
});

process.stdin.on('exit', function (code, signal) {
    console.log('process stdin exit code: %s', code);
});

cmdProcess.stdin.on ('data', function(data){
    console.log('cmd process stdin on data: \n %s', data);
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
