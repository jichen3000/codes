var puts = console.log;

function Bar (name) {
    this.name = name;
}

Bar.prototype.printName = function () {
    puts(this.name);
}

if (require.main === module) {
  require('testhelper');
  
  var bar = new Bar("jc");
  bar.printName();
  puts(typeof bar);
  bar.pp();

  "ok".p();
}