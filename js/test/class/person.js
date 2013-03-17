var Person = function(name){
  this.name = name;
}
Person.prototype = {
  born: function(){
    console.log('I amd born!');
  }
}
// the below line will let the reset the Person prototype. 
// It's a bad way, due to I can't first prototype will replace. 
// I can't use the standard way to create function for the class. 
require('util').inherits(Person,require('events').EventEmitter);

var colin = new Person('colin');
colin.born();