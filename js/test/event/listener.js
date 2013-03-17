var Person =function(name){
  this.emitter = new (require('events')).EventEmitter();
  this.name = name;
  this.emitter.on('newListener',function(event, listener){
    console.log('newListener event: %s, listener: %s', event, listener);
  });
  this.emitter.on('born',function(motherName){
    console.log('event on born');
  });
  this.emitter.on('dead',function(motherName){
    console.log('event on dead');
  });
}
Person.prototype.born = function(motherName){
    console.log("I was born healthly!");
    this.motherName = motherName;
    this.emitter.emit('born', motherName);
  };
Person.prototype = {
  name: "nobody",
  born: function(motherName){
    console.log("I was born healthly!");
    this.motherName = motherName;
    this.emitter.emit('born', motherName);
  },
  dead: function(deadDate){
    console.log("I just deaded dramatically!");
    this.deadDate = deadDate;
    this.emitter.emit('dead', deadDate);
  }
}
var colin = new Person('colin');
colin.emitter.on('born', function(){
  console.log('colin was born!!!');
});
colin.born('mm');
colin.dead('never');

console.log('ok');
