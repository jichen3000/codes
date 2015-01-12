function person(first, last, age, eyeColor){
    this.first = first;
    this.last = last;
    this.age = age;
    this.eyeColor = eyeColor;
}

var myFather = new person("John", "Doe", 50, "blue");
var myMother = new person("Sally", "Rally", 48, "green");
console.log(myFather);
console.log(myMother);

console.log('add property for an instance:');
myFather.nationality = "English";
console.log(myFather);
console.log(myMother);


console.log('add new function for an instance:');
myFather.name = function () {
    return this.first + " " + this.last;
}
console.log(myFather.name());
// console.log(myMother);

console.log('cannot add a  property for a class:');
person.nationality = "English";
console.log(myFather);
console.log(myMother);

console.log('add a  property for a class:');
person.prototype.nationality = "English";
console.log(myFather);
console.log(myMother);
