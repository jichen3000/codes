$().ready(function(){
    $("input#cmd").keydown(input_handler);
    $("input#cmd").focus();
    $("#info").text("Please connect your host, e.g. ssh username:password@ip_or_hostname[:22]");
    //for test
    $("input#cmd").val("ssh root:colin1205@172.16.4.153");
});

var connected = false;

function initialize_page(){
}
function show_connect_info(host){
    $("#info").val("Your host is: "+host);
}

function do_command_result(command_result){
    command_result.split("\n").forEach(function(item){
	$("#out").append($('<p class="cmd cmdresult">'+item+'</p>'));
    });

    scroll2bottom();
}

function clear_div(){
    $("#out").empty();
}
function scroll2bottom(){
    $("html body").animate({ scrollTop: $("html body").prop("scrollHeight") }, 30);
}
var cmdCache=[];
var cmdIndex=cmdCache.length;
function putCmd(cmd){
    if(cmd!=cmdCache[cmdCache.length-1]){
	cmdCache.push(cmd);
    }
    cmdIndex = cmdCache.length;
}
function getCmd(backward){
    if(backward){
	if(cmdIndex>0){
	    cmdIndex -= 1;
	    return cmdCache[cmdIndex];
	}else if(cmdIndex==0){
	    return cmdCache[0];
	}
    }else{
	if(cmdIndex<cmdCache.length-1){
	    cmdIndex += 1;
	    return cmdCache[cmdIndex];
	}else if(cmdIndex==cmdCache.length-1){
	    cmdIndex += 1;
	}
    }
    return '';
}
function doCmd(command){
    if(command=='clear') {
	clear_div();
	return;
    }

    if (connected) {
	//  alert("co");
	$.post("./ssh/cmd/exec",{command:command}, function(data, textStatus){
	    //do nothing
	});
    }else{
	source = new EventSource('/events/start');
	source.onmessage = function(event){
	    do_command_result(event.data);
	};

	$.post("./ssh/connect",{'ssh_paras':command}, function(data,textStatus){
	    if(data=='LOGGED'){
		connected=true;
		$("#info").text("Your ip is: ");
	    }else{
		connected=false;
	    }
	});
    }
    

}
function input_handler(e){
    if(e.keyCode == 13) {
	var cmd = this.value;
	putCmd(cmd);    
	//$("#out").append($('<p class="cmd cmdcontent">'+command+'</p>'));
	this.value="";
	doCmd(cmd);
    }else if(e.keyCode == 38){
	this.value=getCmd(true);
	$("input#cmd").focusEnd();
    }else if(e.keyCode == 40){
	this.value=getCmd(false);
    }
}
