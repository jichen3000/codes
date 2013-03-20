var colin = {};

colin.Person = function (name) {
    "use strict";
    this.name = name;
};

colin.Person.prototype.showName = function () {
    "use strict";
    // this would be the Person instance which invoke this function.
    p("test: this as method pattern: "+this);
    p("It is stored as property of an object!");
    p("'this' would be that object.");
    p("In this case, it would be instance person.");
    p(this.name);
};

var person = new colin.Person("Colin");
person.showName();

function f1 () {
    p("test: this as function pattern: "+this);
    p("It is not a property of a object.");
    p("'this' would be the global object.");
    p("It is a error of design, because for the inner function, it was supposed to be the outer one.");
};
f1();

// workaround for inner function.
colin.double = function () {
    var that = this; // Workaround.
    this.value = 5;
    var helper = function () {
        that.value = that.value + that.value;
    };
    helper(); // Invoke helper as a function. 
};
// Invoke double as a method.
colin.double();
document.writeln(colin.value);


//Use of this style of constructor functions is not recommended.
// Create a constructor function called Quo.
// It makes an object with a status property.
var Quo = function (string) {
    this.status = string;
};
// Give all instances of Quo a public method

// called get_status.
Quo.prototype.get_status = function () { 
    return this.status;
};
// Make an instance of Quo.
var myQuo = new Quo("confused");
document.writeln(myQuo.get_status());     

function add (arg1, arg2) {
    return arg1 + arg2;
}
// Make an array of 2 numbers and add them.
var array = [3, 4];
var sum = add.apply(null, array);    // sum is 7
// Make an object with a status member.
var statusObject = {
    status: 'A-OK'
};
// statusObject does not inherit from Quo.prototype,
// but we can invoke the get_status method on
// statusObject even though statusObject does not have
// a get_status method.
var status = Quo.prototype.get_status.apply(statusObject);
// status is 'A-OK'
