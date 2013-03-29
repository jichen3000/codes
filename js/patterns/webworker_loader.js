colinM.namespace("colinM.test.webworker.loader");
colinM.test.webworker.loader = (function () {
    var self = {},
        p = colinM.p,
        pd = colinM.pd,
        curry = colinM.curry,
        isDefined = colinM.isDefined,
        addSome = curry(colinM.addToDocuemnt,"content"),
        addResult = curry(colinM.addToDocuemnt,"result"),
        cid = document.getElementById,
        file,
        i = 0,
        computer;
    var init = function () {
        addSome('<p>Count numbers: <output id="result"></output></p>');
        addSome('<button onclick="colinM.test.webworker.loader.start()">start</button>');
        addSome('<button onclick="colinM.test.webworker.loader.stop()">stop</button>');
        addSome('<input type="file" onchange="colinM.test.webworker.loader.selectFile(event, this)" id="singlefile"/>');
    };
    self.isWork = function () {
        if(typeof(Worker) === "undefined"){
            alert("Your browser don't support webworker!");
            return false;
        }else{
            p("I work!");
        }
        return true;
    };
    var main = function () {
        init();
        self.isWork();
    };
    window.requestFileSystem  = window.requestFileSystem || window.webkitRequestFileSystem;

    function errorHandler(e) {
      var msg = '';

      switch (e.code) {
        case FileError.QUOTA_EXCEEDED_ERR:
          msg = 'QUOTA_EXCEEDED_ERR';
          break;
        case FileError.NOT_FOUND_ERR:
          msg = 'NOT_FOUND_ERR';
          break;
        case FileError.SECURITY_ERR:
          msg = 'SECURITY_ERR';
          break;
        case FileError.INVALID_MODIFICATION_ERR:
          msg = 'INVALID_MODIFICATION_ERR';
          break;
        case FileError.INVALID_STATE_ERR:
          msg = 'INVALID_STATE_ERR';
          break;
        default:
          msg = 'Unknown Error';
          break;
      };

      console.log('Error: ' + msg);
    }
    self.selectFile = function (event,that) {
        var rfile = that.files[0];
        window.requestFileSystem(window.TEMPORARY, 1048576, function(fs){
            p("in fs");
            fs.root.getFile(rfile.name, {create: true, exclusive: true}, function(fileEntry) {
                p("in fileEntry");
                fileEntry.createWriter(function(fileWriter) {
                    fileWriter.write(rfile); // Note: write() can take a File or Blob object.
                    p("in file write");
                }, errorHandler);
                file = fileEntry;
            });
        }, errorHandler);
    };
    self.start = function () {
        p("start....");
        if(isDefined(file)){
            alert("You should choose you js file firstly");
            return;
        }
        if(typeof(computer) === "undefined"){
            computer = new Worker(file);
        }
        computer.onmessage = function (event) {
            addResult(event.data);
        }
    };
    self.stop = function () {
        p("stop....");
        computer.terminate();
    };
    main();
    return self;
}());
