var http = require('http');
var sys = require('util');
var fs = require('fs');

var timerid = 0;
function addLog(msg){
    console.log("server msg: "+msg);
}
http.createServer(function(req, res) {
    debugHeaders(req);
    
    if (req.headers.accept && req.headers.accept == 'text/event-stream') {
	addLog("in event-stream url:"+req.url);
	if (req.url == '/events/start') {
	    startSSE(req, res);
	} else {
	    res.writeHead(404);
	    res.end();
	}
    } else {
	if(req.url == '/events/stop'){
	    stopSSE(req, res);
	}else{
	    res.writeHead(200, {'Content-Type': 'text/html'});
	    res.write(fs.readFileSync(__dirname + '/button.html'));
	    res.end();
	}
	//res.writeHead(200, {'Content-Type': 'text/html'});
	//res.write(fs.readFileSync(__dirname + '/button.html'));
	//res.end();
    }
}).listen(8000,'172.16.4.153');
console.log('http://172.16.4.153:8000');

function startSSE(req, res) {
    addLog("start sse");
    res.writeHead(200, {
	'Content-Type': 'text/event-stream',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive'
    });
    var id = (new Date()).toLocaleTimeString();

  // Sends a SSE every 5 seconds on a single connection.
    timerid = setInterval(function() {
	constructSSE(res, id, (new Date()).toLocaleTimeString());
    }, 5000);

    constructSSE(res, id, (new Date()).toLocaleTimeString());
}
function stopSSE(req, res) {
    addLog("stop sse");
//    clearInterval(timerid);
} 

function constructSSE(res, id, data) {
    addLog('id: '+id+'  data: '+data);
    res.write('id: ' + id + '\n');
    res.write("data: " + data + '\n\n');
}

function debugHeaders(req) {
    sys.puts('URL: ' + req.url);
    for (var key in req.headers) {
	sys.puts(key + ': ' + req.headers[key]);
    }
    sys.puts('\n\n');
}