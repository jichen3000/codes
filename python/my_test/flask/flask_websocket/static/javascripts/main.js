
// var format_date = function(the_date) {
//     return the_date.getFullYear() + "-" +
//             (the_date.getMonth()+1).toString().rjust(2,"0") + "-" +
//             the_date.getDate().toString().rjust(2,"0") + " " +
//             the_date.getHours().toString().rjust(2,"0") + ":" +
//             the_date.getMinutes().toString().rjust(2,"0") + ":" +
//             the_date.getSeconds().toString().rjust(2,"0");
// }
// var gen_id_by_date = function(the_date) {
//     return the_date.getFullYear() +
//             the_date.getMonth().toString().rjust(2,"0") +
//             the_date.getDate().toString().rjust(2,"0") +
//             the_date.getHours().toString().rjust(2,"0") +
//             the_date.getMinutes().toString().rjust(2,"0") +
//             the_date.getSeconds().toString().rjust(2,"0") +
//             the_date.getMilliseconds().toString().rjust(3,"0");
// }

var id_ele = $("#input-id");
var results_ele = $("#results");


var handle_data = function(data /* , textStatus, jqXHR */ ) {
    // console.log(data);
};
var handle_error = function(xhr, ajaxOptions, thrownError){
    //xhr.status, xhr.statusText
    alert("There is an error on server, "+
        "please contact Colin Ji.(chengji@fortinet.com)!");
};

var message_actions = {
    "log_report_action" : function(value_hash){
        // // console.log(value_hash);
        // open_report_button.removeClass("display-none");
        // // remove then add new one
        // open_report_button.off("click").click(function(event) {
        //     window.open(value_hash["html_path"],'_blank');
        //     // var win = window.open(value_hash["html_path"],'_blank');
        //     // win.focus();
        // });
        add_command_history_row(value_hash);
    },
    "processing_data_action" : function(value_hash){
        // console.log(value_hash);
    }
}
var get_message_value = function(msg) {
    var match_result = msg.match(/value=["'](.+)["']/);
    // var match_result = msg.match(/value=["'](\w+)["']/);
    if ((typeof(match_result) !== 'undefined') && (match_result !== null)) {
        var the_value = match_result[match_result.length-1];
        var value_hash = JSON.parse(the_value);
        return JSON.parse(the_value);
    } else {
        console.error("Error: cannot fine the value from "+msg)
        return null;
    }
}    
var handle_message_value = function(msg) {
    var value_hash = get_message_value(msg);
    if ((typeof(value_hash) !== 'undefined') && (value_hash !== null)) {
        var action_name = value_hash["type"]+"_action";
        var action_fn = message_actions[action_name]
        if (typeof action_fn === 'function'){
            action_fn(value_hash);
        } else {
            console.error("Error: cannot find the action "+action_name);
        }
        // if (value_hash["type"] === "html_report"){
        //     this
        // }
    }        
}    
// var execute_event_source = function(data){
//     // console.log(data);
//     results_ele.append("start...\n");
//     show_status("running");
//     var src = new EventSource('/command_worker/'+id_ele.attr('value'));
//     src.onmessage = function(e) {
//         // console.log(e)
//         if ( e.data === '.'){
//             results_ele.append(e.data);
//         } else  {
//             results_ele.append("\n" + e.data);
//         }
//         console.log("(("+e.data+"))")
//         // results_ele.append(e.data);
//         if ( e.data.includes("<data") ) {
//             handle_message_value(e.data);
//         }
//         window.scrollTo(0,results_ele.position()["top"]+results_ele.height()-350);
//         // window.scrollTo(0,document.body.scrollHeight);
//         if ( e.data.startsWith('!!!end') ) {
//             src.close();
//             show_status("none");
//         }
//     };
// };

// $( "#main-form" ).validate( val_obj ); 
var socket = null;
$("#button-execute").click(function(event) {
    event.preventDefault();
    results_ele.html("")
    
    socket = io.connect(location.protocol + '//' + 
            document.domain + ':' + location.port 
            + "/execution");
    // socket = io.connect(null, {port: location.port, 
    //         namespace:"/execution", 
    //         rememberTransport: false});


    results_ele.append("connecting...\n");
    socket.on('connect', function(){
        socket.emit('exec_event', {data: 'connected'});
    });     
    socket.on('result_event', function(data){
        // console.log(data["msg"]);
        results_ele.append(data["msg"]);
    });     
    socket.on('close_event', function(data){
        console.log(data["msg"]);
        results_ele.append(data["msg"]);
        socket.disconnect();
    });     
});
$("#button-stop").click(function(event) {
    socket.disconnect();
    results_ele.append("force stopped!\n");
});


