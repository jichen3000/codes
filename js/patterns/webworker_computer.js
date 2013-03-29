colinM.namespace("colinM.test.webworker.computer");
colinM.test.webworker.computer = (function () {
    var self = {},
        i = 0;
    this.timedCount = function () {
        i += 1;
        postMessage(i);
        setTimeout(this.timedCount, 500);
    }
    
}());
