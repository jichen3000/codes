p = function (message) {
  document.writeln(message);
};
p_all_properties = function(object) {
  p("all properties:");
  for (property in object){
    p(property+":"+object[property]);
  }
};
p_all_own_properties = function(object) {
  p("all own properties:");
  for (property in object){
    if (object.hasOwnProperty(property)){
      p(property+":"+object[property]);
    }
  }
};
p_all_properties_without_functions = function(object) {
  p("all properties without functions:");
  for (property in object){
    if (typeof object[property] !== 'function'){
      p(property+":"+object[property]);
    }
  }
};


var flight = {
  airline: "China",
  number: 815,
  departure: {
    city: "Hangzhou"
  },
  arrive: {
    city: "Manila"
  },
  count: function(){
    return 11;
  }
};
document.writeln(flight);
document.writeln(flight.mm);
var mm = flight.mm || "I'm mm";
document.writeln(mm);

same_flight = flight;
document.writeln(same_flight===flight);
//document.writeln(flight.mm.ok);
document.writeln("flight prototype:"+flight.prototype);
document.writeln("Object prototype:"+Object.prototype);
p_all_properties(flight);
p_all_own_properties(flight);


p("f type of:"+typeof p);
p("f prototype:"+p.prototype);

var NewClass = function() {};
new_class = new NewClass();
p("new_class typeof:"+typeof new_class);
p_all_properties(new_class);
new_class.prototype = flight;
p_all_properties(new_class);
p("new_class.airline:"+new_class.airline);



if (typeof Object.beget!=='function'){
  Object.beget = function (prototype_object) {
    var F = function() {};
    F.prototype = prototype_object;  
    return new F();
  };
};
var another_flight = Object.beget(flight);
document.writeln("another_flight type of :"+typeof another_flight);
p("another_flight prototype:"+another_flight.prototype);
p_all_properties(another_flight);
p_all_own_properties(another_flight);
p_all_properties_without_functions(another_flight);
p("another_flight.airline:"+another_flight.airline); // use his prototype object property
another_flight.airline="Japan";
p("another_flight.airline:"+another_flight.airline); // use self
delete another_flight.airline;
p("another_flight.airline:"+another_flight.airline); // use his prototype object property

//var third_flight = new flight();
//p_all_properties(third_flight);


//another_flight.prototype = flight;
//document.writeln("another_flight prototype:"+another_flight.prototype);
  

document.writeln("ok");