// basic form:
// jsLint prefer this
// (function () { 
//     alert('watch out!');
// }());

// other form:
// (function () { 
//     alert('watch out!');
// })();
// The book didn't say the difference
(function () {
    var days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        today = new Date(),
        msg = 'Today is ' + days[today.getDay()] + ', ' + today.getDate();
    console.log(msg);
}()); // "Today is Fri, 13"

(function () {
    var days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        today = new Date(),
        msg = 'Today is ' + days[today.getDay()] + ', ' + today.getDate();
    console.log(msg);
})(); // "Today is Fri, 13"

// this way makes the code more interoperable in environments outside the browser:
(function (global) {
    // access the global object via `global`
}(this));

//Immediate Object Initialization
// A drawback of this pattern is that most JavaScript minifiers may not minify this pattern 
// as efficiently as the code simply wrapped into a function.
({
    // here you can define setting values 
    // a.k.a. configuration constants 
    maxwidth: 600,
    maxheight: 400,
    // you can also define utility methods 
    gimmeMax: function () {
        return this.maxwidth + "x" + this.maxheight; 
    },
    // initialize
    init: function () {
        console.log(this.gimmeMax());
        // more init tasks... 
    }
}).init();
    