MYAPP.namespace('MYAPP.utilities.array'); 

MYAPP.utilities.array = (function () {
    // dependencies
    var uobj = MYAPP.utilities.object,
    ulang = MYAPP.utilities.lang,
    // private properties 
    array_string = "[object Array]", 
    ops = Object.prototype.toString;
    // private methods 
    // ...
    // end var
    // optionally one-time init procedures 
    // ...
    // public API 
    return {
        inArray: function (needle, haystack) {
            for (var i = 0, max = haystack.length; i < max; i += 1) {
                if (haystack[i] === needle) {
                    return true; 
                }
            } 
        },
        isArray: function (a) {
            return ops.call(a) === array_string; 
        }
    // ... more methods and properties 
    };
}());

// revealing
// notice, just last part is different.
MYAPP.utilities.array = (function () {
    // private properties
    var array_string = "[object Array]",
    ops = Object.prototype.toString,
    // private methods
    inArray = function (haystack, needle) {
        for (var i = 0, max = haystack.length; i < max; i += 1) { 
            if (haystack[i] === needle) {
                return i; 
            }
        }
        return −1; 
    },
    isArray = function (a) {
        return ops.call(a) === array_string; 
    };
    // end var
    // revealing public API
    return {
        isArray: isArray,
        indexOf: inArray 
    };
}());