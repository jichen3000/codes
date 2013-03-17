var spawn = require('child_process').spawn;
var util = require('util');
var events = require('events');

function SshClient(address, username, password, port){
    var self = this;
    this.address = address;
    this.username = username;
    this.password = password;
    this.port = port;
    this.connected = false;
    this.emitter= new events.EventEmitter();
    function addLog(msg){
	console.log('  ssh client:: %s',msg);
    }
    function getSshParameters(self){
	//return self.username+'@'+self.address+' -p '+self.port;
	return [self.username+'@'+self.address,'-p '+self.port];
    }
    function setupEvents(self){
	addLog('ssh setup events');
	self.ssh.stdin.on('data', function(data){
	    addLog('ssh stdin on data: '+data);
	    return self.emitter.emit('data',data);
	});
	self.ssh.stdin.on('close', function(){
	    addLog('ssh stdin on close');
	    //return self.emitter.emit('data','close');
	});
	self.ssh.stdout.on('data', function(data){
	    addLog('ssh stdout on data: '+data);
	    return self.emitter.emit('data',data);
	});
	self.ssh.stdout.on('close', function(data){
	    addLog('ssh stdout on close');
	    //return self.emitter.emit('data',data);
	});
	self.ssh.stderr.on('data', function(data){
	    addLog('ssh stderr on data: '+ data);
	    return self.emitter.emit('data',data);
	});
	self.ssh.on('exit', function(){
	    addLog('ssh on exit.');
	    self.connected = false;
	    self.emitter.removeAllListeners('data');
	    self.ssh.stdout.removeAllListeners('data');
	    self.ssh.stderr.removeAllListeners('data');
	    self.ssh.removeAllListeners('data');
	    self.emitter.emit('exit', self.address);
	});
	addLog('ssh setup over!');
    }
    this.connect = function(callback){
	addLog('ssh connect');
	if(this.connected) return;
	//this.ssh = spawn('ssh',getSshParameters(this));
	this.ssh = spawn('expect', [__dirname+'/login.exp',
                                    this.address,this.username,
				    this.password,this.port,
				    "-o ConnectTimeout=10"]);
	setupEvents(this);
	callback();
    }
}

module.exports = SshClient;