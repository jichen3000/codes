function dd(msg,value){
  if(value){
    console.log(msg+": "+value);
  }else{
    console.log(msg);
  }
}

process.stdin.resume();
//process.stdin.setEncodeing('utf8');
process.stdin.on('drain',function(){
  dd('process.stdin.on drain');
});
process.stdin.on('error',function(exception){
  dd('process.stdin.on error, exception:',exception);
});
process.stdin.on('close',function(){
  dd('process.stdin.on close');
});
process.stdin.on('pipe',function(src){
  dd('process.stdin.on pipe, src',src);
});
process.stdin.on('data', function (chunk) {
  process.stdout.write('data: ' + chunk);
  process.stdin.destroy();
});
process.stdout.on('data', function (chunk) {
  dd('process.stdout.on data, data:',chuck);
});