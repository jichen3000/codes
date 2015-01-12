var afterAll = require('after-all');
var next = afterAll(done);

setTimeout(next(function () {
    console.log('step two.');
}), 500);

setTimeout(next(function () {
    console.log('step one.');
}), 100);

function done () {
    console.log("done");
}

