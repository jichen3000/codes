Function.prototype.set_method = function(name,func) {
    this.prototype[name] = func;
    return this;
};

Number.set_method('integer', function () {
    return Math[this < 0 ? 'ceil' : 'floor'](this);
});

String.set_method('trim', function () {
    return this.replace(/^\s+|\s+$/g, '');
});

document.writeln('"' + " neat ".trim() + '"');

// Make a factorial function with tail
// recursion. It is tail recursive because
// it returns the result of calling itself.
// JavaScript does not currently optimize this form.

var factorial = function factorial (i, a) {
    a = a || 1;
    if (i < 2) {
        return a;
    };
    return factorial(i - 1, a * i);
}

