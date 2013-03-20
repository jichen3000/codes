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