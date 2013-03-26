var alien = {
    sayHi: function (who) {
        return "Hello" + (who ? ", " + who : "") + "!"; 
    }
};
console.log(alien.sayHi('world')); // "Hello, world!" 
console.log(alien.sayHi.apply(null, ["humans"])); // "Hello, humans!"