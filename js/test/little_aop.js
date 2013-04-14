// Thoughts: what's the differences between AOP and event.
// event, will just have on and trigger functions
// on function's have event_name, callback, context.
// trigger function can be invoked automatcially or manually.
// you can put many callbacks on one function, then they will be invoked one by one.
// IN SHORT, event just define a list of functions which will be invoked by trigger and on host object.
// trigger may have been already impletement on the host object. 

// AOP, most use the before, after, wrap functions.
// they will stick on some function called host function 
// and will be invoked when host function run.
var colinM = colinM || {};
colinM.testFuncs = (function () {
    var self = {};
    _.extend(self, colinM);
    self.f1 = function (msg) {
        self.p("f1");
        self.p("f1 msg:"+ msg);
    };
    self.f2 = self.f1;
    return self;
}());
colinM.littleAOP = (function () {
    var self = {};
    self.after = function (funName, func) {
        if (this.hasOwnProperty(funName) && _.isFunction(this[funName])){
            var original = this[funName];
            this[funName] = function () {
                original.apply(this, arguments);
                func.apply(this, arguments);
            };
        };
    };
    return self;
}());
_.extend(colinM.testFuncs, colinM.littleAOP);
colinM.testFuncs.after("f1", function (msg) {
    console.log("after f1");
    console.log("after f1 msg:" + msg);
});
colinM.testFuncs.f1(123);

// InvalidAspect = new Error("Missing a valid aspect. Aspect is not a function.");
// InvalidObject = new Error("Missing valid object or an array of valid objects.");
// InvalidMethod = new Error("Missing valid method to apply aspect on.");

// function doBefore(beforeFunc,func){
//     return function(){
//         beforeFunc.apply(this,arguments);
//         return func.apply(this,arguments);
//     };  
// }

// function doAfter(func, afterFunc){
//     return function(){
//         var res = func.apply(this,arguments);
//         afterFunc.apply(this,arguments);
//         return res;   
//     };
// }

// Aspects = function(){};
// Aspects.prototype={
//     _addIntroduction : function(intro, obj){
//          for (var m in intro.prototype) {
//               obj.prototype[m] = intro.prototype[m];
//             }
//         },

//     addIntroduction : function(aspect, objs){
//         var oType = typeof(objs);

//         if (typeof(aspect) != 'function')
//         throw(InvalidAspect);

//         if (oType == 'function'){
//             this._addIntroduction(aspect, objs);
//         }
//         else if (oType == 'object'){
//             for (var n = 0; n < objs.length; n++){
//                 this._addIntroduction(aspect, objs[n]);
//             }
//         }
//         else{
//             throw InvalidObject;
//         }
//     },

//     addBefore : function(aspect, obj, funcs){
//           var fType = typeof(funcs);

//           if (typeof(aspect) != 'function')
//             throw(InvalidAspect);

//           if (fType != 'object')
//             funcs = Array(funcs);

//           for (var n = 0; n < funcs.length; n++){
//             var fName = funcs[n];
//             var old = obj.prototype[fName];

//             if (!old)
//               throw InvalidMethod;

//             var res = doBefore(aspect,old)
//             obj.prototype[fName] = res;
//         }
//     },

//     addAfter : function(aspect, obj, funcs) {
//           if (typeof(aspect) != 'function')
//             throw InvalidAspect;

//           if (typeof(funcs) != 'object')
//             funcs = Array(funcs);

//           for (var n = 0; n < funcs.length; n++)
//           {
//             var fName = funcs[n];
//             var old = obj.prototype[fName];

//             if (!old)
//               throw InvalidMethod;

//             var res = doAfter(old,aspect);
//             obj.prototype[fName] = res;
//           }
//         },

//     addAround : function(aspect, obj, funcs){
//           if (typeof(aspect) != 'function')
//             throw InvalidAspect;

//           if (typeof(funcs) != 'object')
//             funcs = Array(funcs);

//           for (var n = 0; n < funcs.length; n++)
//           {
//             var fName = funcs[n];
//             var old = obj.prototype[fName];
//             if (!old)
//               throw InvalidMethod;

//             var res = aspect(old);
//             obj.prototype[fName] = res;
//           }

//           return true;
//         }
// }
