var add = function (a, b) {
    return a + b;
};
// var curry = function () {
//     var concat = Array.prototype.concat,
//         args = concat.apply([], arguments),
//         fun = args.shift();
//     return function () {
//         return fun.apply(this, concat.apply(args,arguments));
//     }
// };
var curry = function (func) {
    var slice = Array.prototype.slice,
        args = slice.call(arguments,1);
    return function () {
        return func.apply(this, args.concat(slice.call(arguments)));
    }
};
var p = function (str) {
    console.log(str);
};

p(add(3,5));
var add3 = curry(add,3);
p(add3(5));