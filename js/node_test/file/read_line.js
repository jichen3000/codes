var fs = require('fs');

var readLinesSync = function (filePath) {
  var data = fs.readFileSync(filePath, {encoding: 'utf-8'});
  return data.split(/\r?\n/);
}

var getLine = function (lines, lineNo) {
  return lines[lineNo-1];
}

if (require.main === module){
  lines = readLinesSync('content.txt');
  console.log(lines);
  console.log(getLine(lines,2));
  console.log("end!");
}