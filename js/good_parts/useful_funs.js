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

var simple_test = function (a1, a2, a3) {
    p(a1+a2+a3);
}

Function.prototype.curry = function () {
    var slice = Array.prototype.slice
    var args = slice.apply(arguments);
    var self = this;
    return function () {
        return self.apply(null,args.concat(slice.apply(arguments)));
    };
};

var st2 = simple_test.curry("3");
st2("1","2");


//memorize
var fibonacci = function (n) {
    return n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2);
};

var fibonacci = (function () { 
    var memo = [0, 1];
    var fib = function (n) {
        var result = memo[n];
        if (typeof result !== 'number') {
            result = fib(n - 1) + fib(n - 2);
            memo[n] = result;
        }
        return result;
    };
    return fib; 
}());

// 将上面的函数一般化后的函数
// 还不是最好的，因为formula只支持一个参数
var memoizer = function (memo, formula) {
    var recur = function (n) {
        var result = memo[n];
        if (typeof result !== 'number') {
            result = formula(recur, n);
            memo[n] = result;
        }
        return result;
    };
    return recur;
};

var fibonacci = memoizer([0, 1], function (recur, n) {
    return recur(n - 1) + recur(n - 2);
});
var factorial = memoizer([1, 1], function (recur, n) {
    return n * recur(n - 1);
});


var fibonacci = _.memoize(function (n) {
    return n < 2 ? n : fibonacci(n-1) + fibonacci(n-2);
});
for (var i = 0; i <= 10; i += 1) {
    document.writeln('// ' + i + ': ' + fibonacci(i));
}


