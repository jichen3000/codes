//Define a functional object to hold persons in javascript
var Person = function (name) {
    this.name = name;
};

//Add dynamically to the already defined object a new getter
Person.prototype.getName = function () {
    return this.name;
};

//Create a new object of type Person
// 如果函数被以new的方式调用，且返回值不是一个对象，则返回this（该新对象）。
// 这时的this，其实就是Person.prototype
var john = new Person("John");

//Try the getter
p(john.getName());

Person.prototype.aliseName = "colin";

//If now I modify person, also John gets the updates
Person.prototype.sayMyName = function () {
    p('Hello, my name is ' + this.getName());
};

//Call the new method on john
john.sayMyName();

//Create a new object of type Customer by defining its constructor. It's not 
//related to Person for now.
var Customer = function (name) {
    this.name = name;
};

//Now I link the objects and to do so, we link the prototype of Customer to 
//a new instance of Person. The protype is the base that will be used to 
//construct all new instances and also, will modify dinamically all already 
//constructed objects because in Javascript objects retain a pointer to the 
//prototype
Customer.prototype = new Person();

//Now I can call the methods of Person on the Customer, let's try, first 
//I need to create a Customer.
var myCustomer = new Customer('Dream Inc.');
myCustomer.sayMyName();

//If I add new methods to Person, they will be added to Customer, but if I
//add new methods to Customer they won't be added to Person. Example:
Customer.prototype.setAmountDue = function (amountDue) {
    this.amountDue = amountDue;
};
Customer.prototype.getAmountDue = function () {
    return this.amountDue;
};

//Let's try:
myCustomer.setAmountDue(2000);
p(myCustomer.getAmountDue());


/*

Every JavaScript object has an internal property called [[Prototype]]. 
If you look up a property via obj.propName or obj['propName'] and the object does not have such a property - 
which can be checked via obj.hasOwnProperty('propName') - 
the runtime looks up the property in the object referenced by [[Prototype]] instead. 
If the prototype-object also doesn't have such a property, its prototype is checked in turn, 
thus walking the original object's prototype-chain until a match is found or its end is reached.

Some JavaScript implementations allow direct access to the [[Prototype]] property, 
eg via a non-standard property named __proto__. 
In general, it's only possible to set an object's prototype during object creation: 
If you create a new object via new Func(), 
the object's [[Prototype]] property will be set to the object referenced by Func.prototype.


This allows to simulate classes in JavaScript, 
although JavaScript's inheritance system is - as we have seen - prototypical, 
and not class-based:

Just think of constructor functions as classes and the properties of the prototype 
(ie of the object referenced by the constructor function's prototype property) as shared members, 
ie members which are the same for each instance. 
In class-based systems, methods are implemented the same way for each instance, 
so methods are normally added to the prototype, 
whereas an object's fields are instance-specific and therefore added to the object itself during construction.



*/
