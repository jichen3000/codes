var colinM = colinM || {};

colinM.p = function (str) {
    console.log(str);
}
var p = colinM.p;

colinM.namespace = function (namespaceStr, parentNamespace) {
    var names = namespaceStr.split('.'),
        parent = parentNamespace || window,
        i;
    for(i = 0; i < names.length; i++) {
        parent[names[i]] = parent[names[i]] || {};
        parent = parent[names[i]];
    }
    return parent;
};

var nowM = colinM.namespace("colin.test.mm");
var nowM = colinM.namespace("colin.test.mm",colinM);
colinM.tt = null;
var nowM = colinM.namespace("colinM.tt.mm");
p(nowM);


// Declaring Dependencies
var myFunction = function () { // dependencies
    var event = YAHOO.util.Event, 
        dom = YAHOO.util.Dom;

    // use event and dom variables
    // for the rest of the function... 
};