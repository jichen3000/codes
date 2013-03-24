p("This is fro chapter 4!");

var add = function(a,b){
  p(this);
  p(arguments);
  return a+b;
};
p("add:"+add);
p_all_properties(add);
add(1,2);
p(add(1,2,3));

p("");
var my_object={age:32};
my_object.grow=function(){
  p(this);
  p("pre age:"+this.age);
  this.age++;
  p("after age"+this.age);
  var inner_this = this;
  inner_f = function(){p(this);p(inner_this.age)};
  inner_f();
}
my_object.grow();

p("");
var Quo = function(status){
  p(this);
  this.status = status;
}
Quo.prototype.get_status = function(){return this.status};
my_quo = new Quo("new");
p(my_quo.status);
p(my_quo.get_status());
p(my_quo.prototype);

p("");
var add_array = [3,4];
var sum = add.apply(my_object,add_array);
p(sum);

var ok_object = {status:'OK'};
p(Quo.prototype.get_status.apply(ok_object));

var sum = function(){
  var i, sum=0;
  for(i=0; i<arguments.length; i++){
    sum += arguments[i];
  }
  return sum;
}
p(sum(1,2,3,4,5))

p("");
var add_with_exceptions=function(a,b){
  if(typeof a !=="number" || typeof b !== "number"){
    throw {
      name: 'TypeError',
      message: 'add needs number'
    };
  }
  return a+b;
}

p(add_with_exceptions(2,1));
try{
  add_with_exceptions('');
}catch(e){
  p(e.name+";"+e.message);
}

Function.prototype.method = function(name,func){
  this.prototype[name] = func;
  return this;
}
Number.method('to_int',function(){
  return Math[this<0 ? 'ceil' : 'floor'](this);
});
p (Math.ceil(-10/3));
p ((-10/3).to_int());
p ((10/3).to_int());

p("");
String.prototype.trim = function(){
  return this.replace(/^\s+|\s+$/g,'');
}
p("'"+"  mmm ".trim()+"'");
p("ok");