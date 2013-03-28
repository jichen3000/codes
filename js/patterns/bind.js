

var bind = function (obj, fun) {
    return function () {
        return fun.apply(obj, Array.prototype.slice.call(arguments));
    };
};

var one = {
    name: "one",
    say: function (greet) {
        return greet +", " + this.name;
    }
};

var p = function (str) {
    console.log(str);
};

p(one.say('hi'));

var two = {
    name: "tow"
};

p(one.say.call(two,'hello'));

var say = one.say
p(say('hoho'));

var yetanother = {
    name: "yet another",
    method: function (callback) {
        return callback('Holo');
    }
};
p(yetanother.method(one.say));

var twosay = bind(two,one.say);
p(twosay("mm"));

var twosay2 = one.say.bind(two);
p(twosay2("kk"));