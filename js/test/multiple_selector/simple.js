$(function(){
    $("#select-choose").multiSelect({
        selectableHeader: "<div class='custom-header'>Selectable items</div>",
        selectionHeader: "<div class='custom-header'>Selection items</div>",
        selectableFooter: "<div class='custom-header'>Selectable footer</div>",
        selectionFooter: "<div class='custom-header'>Selection footer</div>"
    });
    $("#button-choose").click(function(event){
        console.log($("#select-choose").val());
    });
});