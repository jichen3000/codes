function Mammal(name){
    this.name = name;
    this.offspring = [];
}
Mammal.prototype.haveABaby = function () {
    var newBaby = new Mammal("Baby " + this.name);
    this.offspring.push(newBaby);
    return newBaby;
}
Mammal.prototype.toString = function () {
    return '[Mammal "'+this.name+'"]';
}

// Mammal ---> Mammal.prototype ---> null;
// Mammal's superclass is Mammal.prototype, Mammal.prototype's superclass is null
// js cannot get supercalss name.

function Cat(name){ 
    this.name=name;
}
Cat.prototype = new Mammal();
Cat.prototype.toString=function(){ 
    return '[Cat "'+this.name+'"]';
} 
cat1 = new Cat('cc');
console.log(cat1);
