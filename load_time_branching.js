// init-time/load-time branching
// the function will be detemined when it is first loaded.

// the interface 
var utils = {
    addListener: null,
    removeListener: null 
};
// the implementation
if (typeof window.addEventListener === 'function') {
    utils.addListener = function (el, type, fn) {
        el.addEventListener(type, fn, false); 
    };
    utils.removeListener = function (el, type, fn) {
        el.removeEventListener(type, fn, false); 
    };
} else if (typeof document.attachEvent === 'function') { // IE 
    utils.addListener = function (el, type, fn) {
        el.attachEvent('on' + type, fn); 
    };
    utils.removeListener = function (el, type, fn) {
        el.detachEvent('on' + type, fn); 
    };
} else { // older browsers
    utils.addListener = function (el, type, fn) {
        el['on' + type] = fn; 
    };
    utils.removeListener = function (el, type, fn) {
        el['on' + type] = null; 
    };
}