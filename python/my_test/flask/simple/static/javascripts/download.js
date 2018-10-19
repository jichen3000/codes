var download_content = function(filename, ele_id, mime_type) {
    var elHtml = document.getElementById(ele_id).innerHTML;
    var link = document.createElement('a');
    mime_type = mime_type || 'text/plain';

    link.setAttribute('download', filename);
    link.setAttribute('href', 'data:' + mime_type + ';charset=utf-8,' + encodeURIComponent(elHtml));
    link.click(); 
}

$('#button-download').click(function(){
    download_content('command.log', 'results','text/plain');
});