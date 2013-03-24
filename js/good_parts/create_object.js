// Create a maker function called quo. It makes an
// object with a get_status method and a private
// status property.

var quo = function (status) {
    return {
        get_status: function () {
            return status;
        }
    };
};
// Make an instance of quo.
var myQuo = quo("amazed");
document.writeln(myQuo.get_status( ));


// Define a function that sets a DOM node's color
// to yellow and then fades it to white.
var fade = function (node) {
    var level = 1;
    var step = function () {
        var hex = level.toString(16); 
        node.style.backgroundColor = '#FFFF' + hex + hex; 
        if (level < 15) {
            level += 1;
            setTimeout(step, 100);
        }
    };
    setTimeout(step, 100);
};
fade(document.body);

// bad example.
// i will always the nodes.length-1, since closure will let inner funcation access the i reference, not i's value.
// var add_the_handlers = function (nodes) {
//     var i;
//     for (i = 0; i < nodes.length; i += 1) {
//         nodes[i].onclick = function (e) {
//             alert(i); 
//         };
//     } 
// };
// add_the_handlers(document.body.childNodes);

// BETTER EXAMPLE
// Make a function that assigns event handler functions to an array of nodes.
// When you click on a node, an alert box will display the ordinal of the node.
var add_the_handlers = function (nodes) {
    var helper = function (i) {
        return function (e) {
            alert(i);
        }; 
    };
    var i;
    for (i = 0; i < nodes.length; i += 1) {
        nodes[i].onclick = helper(i);
    }
};


