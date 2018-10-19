String.prototype.ljust = function( width, padding ) {
	padding = padding || " ";
	padding = padding.substr( 0, 1 );
	if( this.length < width )
		return this + padding.repeat( width - this.length );
	else
		return this;
}
String.prototype.rjust = function( width, padding ) {
	padding = padding || " ";
	padding = padding.substr( 0, 1 );
	if( this.length < width )
		return padding.repeat( width - this.length ) + this;
	else
		return this;
}
$(function() {

    var format_date = function(the_date) {
        return the_date.getFullYear() + "-" +
                (the_date.getMonth()+1).toString().rjust(2,"0") + "-" +
                the_date.getDate().toString().rjust(2,"0") + " " +
                the_date.getHours().toString().rjust(2,"0") + ":" +
                the_date.getMinutes().toString().rjust(2,"0") + ":" +
                the_date.getSeconds().toString().rjust(2,"0");
    }
    var gen_id_by_date = function(the_date) {
        return the_date.getFullYear() +
                the_date.getMonth().toString().rjust(2,"0") +
                the_date.getDate().toString().rjust(2,"0") +
                the_date.getHours().toString().rjust(2,"0") +
                the_date.getMinutes().toString().rjust(2,"0") +
                the_date.getSeconds().toString().rjust(2,"0") +
                the_date.getMilliseconds().toString().rjust(3,"0");
    }

    var id_ele = $("#input-id");
    var results_ele = $("#results");
    var ip_ele = $("#input-ip"),
        port_ele = $("#input-port"),
        username_ele = $("#input-username"),
        password_ele = $("#input-password"),
        repeat_times_ele = $("#input-repeat-times"),
        sleep_ele = $("#input-sleep"),
        commands_ele = $("#input-commands"),
        config_comment_ele = $("#input-config-comment"),
        delay_minutes_ele = $("#input-delay-minutes")
    var get_form_values = function() {
        return {
            "id":id_ele.val(),
            "ip":ip_ele.val(),
            "port":parseInt(port_ele.val()),
            "username":username_ele.val(),
            "password":password_ele.val(),
            "repeat_times":parseInt(repeat_times_ele.val()),
            "sleep":parseInt(sleep_ele.val()),
            "commands":commands_ele.val(),
            "config_comment":config_comment_ele.val(),
            "delay_minutes":parseInt(delay_minutes_ele.val())
        }
    };
    var show_status = function(status) {
        var stop_button = $("#button-stop");
        var download_button = $("#button-download");
        var execute_button = $("#button-execute");
        var loader_div = $("#loader");
        if (status === "none") {
            stop_button.addClass("display-none");
            //download_button.addClass("display-none");
            loader_div.addClass("display-none");
            execute_button.prop("disabled", false);
        } else if (status === "running") {
            stop_button.removeClass("display-none");
            download_button.removeClass("display-none");
            loader_div.removeClass("display-none");
            execute_button.prop("disabled", true);
        }
    }; 

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
    var execute_event_source = function(data){
        // console.log(data);
        results_ele.append("start...\n");
        show_status("running");
        var src = new EventSource('/command_worker/'+id_ele.attr('value'));
        src.onmessage = function(e) {
            // console.log(e)
            if ( e.data === '.'){
                results_ele.append(e.data);
            } else  {
                results_ele.append("\n" + e.data);
            }
            console.log("(("+e.data+"))")
            // results_ele.append(e.data);
            if ( e.data.includes("<data") ) {
                handle_message_value(e.data);
            }
            window.scrollTo(0,results_ele.position()["top"]+results_ele.height()-350);
            // window.scrollTo(0,document.body.scrollHeight);
            if ( e.data.startsWith('!!!end') ) {
                src.close();
                show_status("none");
            }
        };
    };
    $("#button-execute").click(function(event) {
        event.preventDefault();
        results_ele.html("")
        cur_id = gen_id_by_date(new Date(Date.now()));
        id_ele.attr('value',cur_id);
        var valid = true;
        if (valid) {
            var values = get_form_values();
            // console.log(values);
            $.ajax({
                url: '/commands_info/',
                type: 'POST',
                data: values,
                success: execute_event_source,
                error: handle_error
            });


        }
    });
    $("#button-stop").click(function(event) {
        $.ajax({
            url: '/command_worker/'+id_ele.attr('value'),
            type: 'POST',
            data: {
                _method: 'delete'
            },
            success: handle_data,
            error: handle_error
        });
        show_status("none");
    });

    var add_command_history_row =function(value_hash){
        var the_config = value_hash["config"];
        // 
        // var existed_tr_ele = $('tr[id="worker127.0.0.1-20170628150458359"]');
        var existed_tr_ele = $('tr[id="'+the_config["worker_id"]+'"]');
        var log_name = the_config["log_name"].split("/").slice(-1)[0];
        if (existed_tr_ele.length == 0){
            var restore_button = $('<button class="btn btn-info btn-sm restore-btn">'+
                    'Restore</button>');
            restore_button.on("click", function(){
                ip_ele.val(the_config["ip"]);
                port_ele.val(the_config["port"]);
                username_ele.val(the_config["username"]);
                password_ele.val(the_config["password"]);
                repeat_times_ele.val(the_config["repeat_times"]);
                sleep_ele.val(the_config["sleep"]);
                commands_ele.val(the_config["commands"]);
                config_comment_ele.val(the_config["config_comment"]);
                delay_minutes_ele.val(the_config["delay_minutes"]);
                if (delay_minutes_ele.val() === "") {
                    delay_minutes_ele.val(0);
                }

                $("#alert-info").removeClass("display-none");
                setTimeout(function(){
                    $("#alert-info").addClass("display-none");
                }, 2000);
            });
            $("#command-history").find('tbody').prepend(
                $('<tr id="'+the_config["worker_id"]+'" >').append(
                    $('<td>').text(value_hash["start_time"])
                ).append(
                    $('<td>').text(value_hash["config"]["ip"])
                ).append(
                    $('<td>').text(value_hash["config"]["username"])
                ).append(
                    $('<td>').text(value_hash["config"]["repeat_times"])
                ).append(
                    $('<td>').text(value_hash["config"]["config_comment"])
                            .append(restore_button)
                ).append(
                    $('<td class="td-log-path">').append($('<div>')
                    .append($('<a>').attr('href',the_config["log_name"])
                    .attr('target','_blank').text(log_name)))
                )
            );
        } else {
            // var html_path_td = existed_tr_ele.find(".td-html-path");
            // html_path_td.append($('<div>').append($('<a>').attr('href',value_hash["html_path"])
            //         .attr('target','_blank').text(html_name)))
        }
    }

    var refresh_history = function(){
        $.ajax({
            url: '/history_info/50',
            type: 'get',
            dataType: 'json',
            success: function(data){
                // console.log(data);
                data["data"].forEach(function(entry){
                    console.log(entry);
                    add_command_history_row(entry);
                    // var result_list = entry["result_list"];
                    // if (typeof(result_list) === 'undefined'){
                    //     add_command_history_row(entry);
                    // } else {
                    //     result_list.forEach(function(result_item){
                    //         var new_entry = Object.assign({}, entry, result_item)
                    //         add_command_history_row(new_entry);
                    //     });                        
                    // }
                });
            },
            error: handle_error
        });
    }

    // refresh_history();
    show_status("none");

});
