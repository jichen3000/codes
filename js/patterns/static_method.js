// constructor
var Gadget = function () {};
// a static method 
Gadget.isShiny = function () {
    // this will be Gadget constructor.
    return "you bet"; 
};
// a normal method added to the prototype 
Gadget.prototype.setPrice = function (price) {
    this.price = price; 
};

// calling a static method 
Gadget.isShiny(); // "you bet"
// creating an instance and calling a method 
var iphone = new Gadget(); 
iphone.setPrice(500);

typeof Gadget.setPrice; // "undefined" 
typeof iphone.isShiny; // "undefined"