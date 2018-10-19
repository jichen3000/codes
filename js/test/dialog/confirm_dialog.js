$(function(){

    $("#button-open-dialog").click(function(event) {
        $("#dialog-confirmation").modal();
    });
    $("#button-dialog-confirm").click(function(event) {
        // use the below one to close
        // $("#dialog-confirmation").modal('toggle');
        console.log("123");
    });


});