var fs = require('fs');


var readSome = function (filePath) {
  // show how to read a file.
  console.log(filePath);

  fs.readFile(filePath, {encoding: 'utf-8'}, function readData (err, data) {
    console.log("in read");
    if (err) throw err;
    console.log(data);
    return true;
  });
  console.log("end");
}

var readSomeSync = function (filePath) {
  console.log(filePath);
  data = fs.readFileSync(filePath, {encoding: 'utf-8'});
  console.log(data);
  console.log("endSync");
  return data;
}



if (require.main === module){
  readSome("content.txt");
  readSomeSync("content.txt");
}

