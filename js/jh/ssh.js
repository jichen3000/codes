var fu = require("./fu"),
SshClient = require("./exec_ssh"),
util = require("util"),
url = require("url"),
qs = require("querystring");



fu.listen(1337,  "172.16.4.153");
fu.addGet("/", fu.staticHandler("console.html"));
fu.addGet("/favicon.ico", fu.staticHandler("favicon.ico"));
fu.addGet("/jquery-1.6.2.min.js", fu.staticHandler("jquery-1.6.2.min.js"));
fu.addGet("/client.js", fu.staticHandler("client.js"));
fu.addGet("/jh.css", fu.staticHandler("jh.css"));


function addLog(msg){
    console.log("  server:: "+msg);
}
var ssh = null;
var eventRes = null;
function sendToEvent(msg_lines){
    var id = (new Date()).toLocaleTimeString();
    addLog('id: '+id+'  data: '+msg_lines);
    eventRes.write('id: ' + id + '\n');
    msg_lines.split("\n").forEach(function(item){
	eventRes.write("data: " + item + '\n');
    });
    eventRes.write("data: " + '\n\n');
}
fu.addPost("/events/start", function(req, res){
    if (req.headers.accept && req.headers.accept == 'text/event-stream') {
	addLog("in event-stream url:"+req.url);
	addLog("start sse");
	res.writeHead(200, {
	    'Content-Type': 'text/event-stream',
	    'Cache-Control': 'no-cache',
	    'Connection': 'keep-alive'
	});
	eventRes=res;
    }
});
fu.addPost("/ssh/connect", function(req, res){
    var body='';
    req.on('data', function(data){
	body += data;
    });
    function getSshParas(cmd){
	var paras = cmd.substr(4).split(/:|@/);
	if(paras.length<4){
	    paras.push("22");
	}
	return paras;
    }
    req.on('end', function(){
	var input_data = qs.parse(body);
	//var paras = (qs.parse(body)['ssh_paras']).split(/:|@/);
	var paras = getSshParas(qs.parse(body)['ssh_paras']);
	addLog("paras:"+paras); 
	var address = paras[2];
	var username = paras[0];
	var password = paras[1];
	var port = parseInt(paras[3]);
	// LOGING, LOGGED, FAILED
	//var log_status = 'LOGING';
	ssh=new SshClient(address,username,password,port);
	ssh.connect(function(){
	    addLog('test connect');
	});
	function checkLogged(msg){
	    return (msg.indexOf('Login successful')>-1);  
	}
	function checkFailed(msg){
	    return (msg.indexOf('Login failed')>-1);  
	}
	function sshOnData(data){
	    addLog('test ssh emitter on data: ,,,'+data+'...');
	    var result_msg = data.toString();
	    sendToEvent(result_msg);
	}
	ssh.emitter.on('data',function(data){
	    //addLog('test ssh emitter on data: ,,,'+data+'...');
	    var result_msg = data.toString();
	    //sendToEvent(result_msg);
	    sshOnData(data);
	    if(checkLogged(result_msg)){
		ssh.emitter.removeAllListeners('data');
		ssh.emitter.on('data', sshOnData);
		res.simpleText(200, 'LOGGED');
	    }else if(checkFailed(result_msg)){
		ssh.emitter.removeAllListeners('exit');
		ssh.emitter.removeAllListeners('data');
		res.simpleText(400, 'FAILED');
	    }
	});
	ssh.emitter.on('exit', function(){
	    addLog('test ssh emitter on exit');
	    process.stdin.destroy();
	});
	//res.simpleText(200, '');
    });
});
fu.addPost("/ssh/cmd/exec",function(req, res){
    var body=''; 
    req.on('data', function (data) {
	body += data;
    });
    req.on('end', function () {
	var postdata = qs.parse(body);
	addLog('it will exec cmd: '+postdata['command']);
	ssh.ssh.stdin.write(postdata['command']+'\n');
	res.simpleText(200, '');
	//    addLog('req on end, over!');
	//exec.exec_cmd(postdata['command'], function(cmd_result){
	    //console.log("cmd_result: %s", cmd_result);
	  //  res.simpleJSON(200, { result:cmd_result});
	//});
    });
});
