// antipattern
myname = "global"; // global variable 
function func() {
    console.log(myname); // "undefined" 
    console.log(this.myname); // "global" 
    var myname = "local"; 
    console.log(myname); // "local"
} 
func();