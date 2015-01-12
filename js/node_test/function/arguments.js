var puts = console.log;

function something (arg1, arg2) {
  puts(arg1);
  puts(arg2);
  puts(arguments);
  puts("arguments.length:"+arguments.length);
}

if (require.main = module){
  something();
  something(1);
  puts("ok");
}