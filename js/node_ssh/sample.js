
//var SSHClient = require("./NodeSSH");
var SSHClient = require("./index");
var address = '172.16.4.153';
var ssh=new SSHClient(address,'root','colin',22);
var cmds=["uptime","logout"];
function close(addr) {
    console.log('sapmle  Disconnected from '+addr);
}

function data(buffer) {
    s=buffer.toString();
    console.log('sample data, buffer: %s', s);
    if (/logged/.test(s)||/\#/.test(s)||/\$/.test(s)) {
       if (cmd=cmds.shift())
          ssh.write(cmd+"\r\n");
       else ssh.close();
    }
}

function connect() {
    console.log('sample Connected to '+this.address);
    ssh.on('data',data);
}

ssh.on('close',close);


ssh.connect(connect);

