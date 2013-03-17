var spawn = require('child_process').spawn;
var util = require('util');

function sshClient(address,username,password,port){
    console.log('sshClient');
    var self=this;
    this.address=address;
    this.user=username;
    this.line=0;
    this.buffer=null;
    this.exec=function(cmd) {
	console.log('exec');
        if (this.connected) return;
        this.ssh = spawn('expect', [__dirname+'/login.exp',
				    this.address,this.user,password,port,"-o ConnectTimeout=10",cmd]);
        setupEvents(this)
    }
    this.connect=function(connect) {
        console.log('connect '+this.address);
        if (this.connected) return;
        this.ssh = spawn('expect', [__dirname+'/login.exp',
				    this.address,this.user,password,port,"-to ConnectTimeout=10"]);
        setupEvents(this)
        this.c=connect();
	//console.log('this: %s', util.inspect(this));
    }
    this.pipe=function(target) {
	console.log('pipe');
        this.ssh.stdout.pipe(target);
    }
    function setupEvents(self) {
	console.log('setupEvents');
        self.ssh.stdout.on('data', function (data) {
            console.log("in:"+data.toString());
            if (self.connected) {
                return self.emit('data',data);
            }
            if (data.toString().match("logged")) { 
                self.connected=true;
                self.emit('connected',self.address);
                return self.emit('data',data);
            }
            var str = data.toString().substr(0,16);
            if(str == "Connection refuse"){
                self.emit('refused',self.address);
                self.ssh.kill();
                return;
            }
            if(str == "Permission denied"){
                self.emit('denied',self.address);
                self.ssh.kill();
                return;
            }
        });
            
        self.ssh.on("exit",function(){
	    console.log('ssh on exit');
            self.connected=false;
            self.removeAllListeners('data');
            self.ssh.stdout.removeAllListeners('data');
            self.ssh.removeAllListeners();
            self.emit('close',self.address);
        });
    }
    
    this.write=function(data){
	console.log('write');
        console.log("out:"+data.toString());
        this.ssh.stdin.write(data);
    }
    this.close=function(){
	console.log('close');
        this.ssh.kill();
    }
}
require('util').inherits(sshClient,require('events').EventEmitter);
module.exports=sshClient;
