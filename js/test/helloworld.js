var http = require('http');
function start(req, res){
  console.log('req.url:'+req.url);
  res.writeHead(200,{'Content-Type': 'text/plain'});
  res.end('Hello World Colin\n');
}
http.createServer(start).listen(1337, "127.0.0.1");
console.log('Server running at http://127.0.0.1:1337/');

