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

// prototypal
// myMammal.__proto__ will be {}
// myMammal.prototype will be undefined.
var myMammal = {
    name : 'Herb the Mammal', get_name : function () {
        return this.name;
    },
    says : function () {
        return this.saying || '';
    } 
};
// myCat.__proto__ will be myMammal
// myCat.prototype will be undefined.
var myCat = Object.create(myMammal);
myCat.name = 'Henrietta';
myCat.saying = 'meow';
myCat.purr = function (n) {
    var i, s = '';
    for (i = 0; i < n; i += 1) {
        if (s) {
            s += '-';
        }
        s += 'r'; 
    }
    return s; 
};
myCat.get_name = function () {
    return this.says() + ' ' + this.name + ' ' + this.says();
};

// funcational create object.
// this mean will offer private proverty.
// The spec object contains all of the information that the constructor needs to make an instance.
// The my object is a container of secrets that are shared by the constructors in the inheritance chain.
var constructor = function (spec, my) {
    //other private instance variables;
    var that 
    my = my || {};
    //Add shared variables and functions to my 
    that = {};
    //Add privileged methods to that
    // two steps, let the other inner functions to use methodical, not that.methodical
    // reduce the confliction with outside.
    var methodical = function () {
        // do something
    };
    that.methodical = methodical;
    return that;
};

// example fo the above, funcational
var mammal = function (spec) {
    var that = {};
    that.get_name = function () { 
        return spec.name;
    };
    that.says = function () { 
        return spec.saying || '';
    };
    return that;
};
var myMammal = mammal({name: 'Herb'});
var cat = function (spec) {
    spec.saying = spec.saying || 'meow';
    var that = mammal(spec);
    that.purr = function (n) {
        var i, s = '';
        for (i = 0; i < n; i += 1) {
            if (s) {
                s += '-';
            }
            s += 'r'; 
        }
        return s; 
    };
    that.get_name = function () {
        return that.says() + ' ' + spec.name + ' ' + that.says();
    };
    return that;
};
var myCat = cat({name: 'Henrietta'});

// for getting the function of super
Object.prototype.superior = function (name) {
    var that = this,
        method = that[name]; 
    return function () {
        return method.apply(that, arguments);
    };
};
var coolcat = function (spec) {
    // you cannot just write:
    var that = cat(spec),
        super_get_name = that.get_name;
        // super_get_name = that.superior('get_name');
    that.get_name = function (n) {
        return 'like ' + super_get_name() + ' baby'; 
    };
    return that;
};

var myCoolCat = coolcat({name: 'Bix'}); 
var name = myCoolCat.get_name();
p(name);
// 'like meow Bix meow baby'


// event
var eventuality = function (that) {
    var registry = {};
    that.fire = function (event) {
        // Fire an event on an object. The event can be either
        // a string containing the name of the event or an
        // object containing a type property containing the
        // name of the event. Handlers registered by the 'on'
        // method that match the event name will be invoked.
        var array,
            func,
            handler,
            i,
            type = typeof event === 'string' ? event : event.type;
        // If an array of handlers exist for this event, then
        // loop through it and execute the handlers in order.
        if (registry.hasOwnProperty(type)) {
            array = registry[type];
            for (i = 0; i < array.length; i += 1) {
                handler = array[i];
                // A handler record contains a method and an optional
                // array of parameters. If the method is a name, look
                // up the function.
                func = handler.method;
                if (typeof func === 'string') {
                    func = this[func];
                }
            // Invoke a handler. If the record contained
            // parameters, then pass them. Otherwise, pass the
            // event object.
            func.apply(this, handler.parameters || [event]);
            } 
        }
        return this;
    };

    that.on = function (type, method, parameters) {
        // Register an event. Make a handler record. Put it
        // in a handler array, making one if it doesn't yet
        // exist for this type.
        var handler = {
            method: method,
            parameters: parameters
        };
        if (registry.hasOwnProperty(type)) {
            registry[type].push(handler);
        } else {
            registry[type] = [handler];
        }
        return this;
    };
    return that;
};