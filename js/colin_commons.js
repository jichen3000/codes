var colinM = colinM || {};

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

colinM.p = function (str) {
    console.log(str);
};
colinM.pd = function (str) {
    document.writeln(str);
};

colinM.isDefined = function (variable) {
    return (typeof(variable) === "undefined");
};
colinM.addToDocuemnt = function (id, addHtml) {
    var content = document.getElementById(id);
    content.innerHTML += addHtml;
};

colinM.curry = function (func) {
    var slice = Array.prototype.slice,
        args = slice.call(arguments,1);
    return function () {
        return func.apply(this, args.concat(slice.call(arguments)));
    }
};


