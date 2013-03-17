function p(msg){
  $('p#messages').text(msg);
}

function gen_ints (start_int, max_int) {
    var int_arr = [];
    var index = 0;
    for(var value=start_int; value>=0; value--,index++){
        int_arr[index] = value;
    }
    for (value=max_int; value > start_int; value--,index++) {
        int_arr[index] = value;
    }
    return int_arr.join(" ");
}

$(function() {
  $('button#set').click(function(){
    var min_sum = $('input#input_min_sum').val().split("");
    p("Cleared all values in the cells."+gen_ints(min_sum[0],9)+"  :"+gen_ints(min_sum[1],9));
    $('div.tenminute').text(gen_ints(min_sum[0],5));
    $('div.minute').text(gen_ints(min_sum[1],9));
  });    
  $('input#start').click(function(){
//    var min_sum = $('input#input_min_sum').val().split("");
    p("start.");
  });    
});

