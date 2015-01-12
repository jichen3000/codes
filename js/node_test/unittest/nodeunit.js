exports.testSomething = function(test){
    test.expect(1);
    test.ok(true, "this assertion should pass");
    test.done();
};

exports.testSomethingElse = function(test){
    test.ok(false, "this assertion should fail");
    test.done();
};

var suite1 = {
    'test one': function (test) {
        test.ok(true, 'everythings ok');
        setTimeout(function () {
            test.done();
        }, 10);
    },
    'apples and oranges': function (test) {
        test.equal('apples', 'oranges', 'comparing apples and oranges');
        test.done();
    }
};

if (require.main === module) {
    var nodeunit = require('nodeunit');
    console.log(nodeunit);
    nodeunit.runSuite({'suite1': suite1});
    // nodeunit.runTest(exports.testSomethingElse);
    // var reporter = require('nodeunit').reporters.default;
    // reporter.run(exports.testSomethingElse);
}
