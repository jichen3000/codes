var str = "colin\nmm\njc";
var str_arr = str.split("\n");
console.log("arr : %s", str_arr);

str.split("\n").forEach(function(item){
  console.log("item : %s", item);
});
console.log("end.");