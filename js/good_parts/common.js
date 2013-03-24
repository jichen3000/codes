p = function (message) {
  document.writeln(message);
};
p_all_properties = function(object) {
  p("all properties:");
  if (object.length === 0){
    p("none!")
  }
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