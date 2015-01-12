// explain the issue of this
// http://howtonode.org/what-is-this

// Make a function that returns a closure function.
function myModule() {
  var name = "tim", age = 28;
  return function greet() {
    return "Hello " + name + ".  Wow, you are " + age + " years old.";
  }
}
// call `myModule` to get a closure out of it.
var greeter = myModule();
// Call the closure
var result = greeter();
console.log(result);

var Person = {
  name: "Tim",
  age: 28,
  greeting: function () {
    return "Hello " + this.name + ".  Wow, you are " + this.age + " years old.";
  }
};

var result = Person.greeting();
console.log(result); // it will be alright. since this stands for Person.

var greeting = Person.greeting;
var result =  greeting(); // Will get undefined for `this.name` and `this.age`
console.log(result); // since this stands for global object.


var Dog = {
  name: "Alfred",
  age: 110,
  greeting: Person.greeting
}

var result = Dog.greeting(); // This will work and it will show the dog's data.
console.log(result); 

var Alien = {
  name: "Zygoff",
  age: 5432
}

var result = Person.greeting.call(Alien);
console.log(result);  // inject the object Alien as the "this" 

function bind(fn, scope){
  return function () {
    return fn.apply(scope, arguments);
  }
}
Person.greeting = bind(Person.greeting, Person);
var greeting = Person.greeting;
var result =  greeting(); // Will get undefined for `this.name` and `this.age`
console.log(result); // since this stands for global object.