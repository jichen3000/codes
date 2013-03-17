var SshClient = require('./exec_ssh');
var util = require('util');
var address = '172.16.4.153';
var port = 22
var ssh=new SshClient(address,'root','colin',port);
function addLog(msg){
    console.log("  test ssh:: "+msg);
}
  process.stdin.on('data', function (data) {
    addLog('process stdin on data: '+data);
    ssh.ssh.stdin.write(data);
    //process.stdout.write(data);
    process.stdin.end();
    //process.stdout.destroy();
    //ssh.ssh.stdin.destroy();
    addLog('process stdin on data, over!');
  });

  process.stdin.on('close', function () {
      ssh.ssh.stdin.end();
    addLog('process stdin on close.');
  });
  process.stdout.on('data', function () {
    addLog('process stdout on data: '+data);
  });
  process.on('exit', function(){
    addLog('process on exit.');
  });
ssh.connect(function(){
    addLog('test connect');
});
ssh.emitter.on('data',function(data){
  addLog('test ssh emitter on data: '+data);
  //ssh.ssh.stdin.write('colinalfred'+"\r\n");
  
  process.stdin.resume();
  process.stdin.setEncoding('utf8');
  //addLog('ssh.ssh.stdin :%s',util.inspect(ssh));
//  process.stdin.pipe(ssh.ssh.stdin);
  
});
ssh.emitter.on('exit', function(){
    addLog('test ssh emitter on exit');
    process.stdin.destroy();
});