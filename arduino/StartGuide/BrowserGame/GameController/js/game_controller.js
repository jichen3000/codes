var GameController = function (path, threshold) {
    this.arduino = new SerialDevice(path, 38400);
    this.threshold = threshold || 328;
    this.moveLeft = false;
    this.moveRight = false;
    this.xPos = threshold || 328;
    this.buttonPressed = false;
    this.boundOnReadLine = this.onReadLine.bind(this);
    this.arduino.onReadLine.addListener(this.boundOnReadLine);
    this.arduino.connect();
}

GameController.prototype.onReadLine = function (line) {
    const TOLERANCE = 5;
    var attr = line.trim().split(' ');
    if (attr.length == 4) {
        this.moveRight =false;
        this.moveLeft = false;
        var x = parseInt(attr[0]);
        this.xPos=x;
        if (x <= this.threshold - TOLERANCE) {
            this.moveLeft = true;
        } else if ( x >= this.threshold + TOLERANCE) {
            this.moveRight = true;
        }

        this.buttonPressed = (attr[3] == '1');
    }
    var message = 'pos('+ this.xPos+'), '+'moveLeft(' + this.moveLeft + '), ' +
        'moveRight (' + this.moveRight + '), ' + 
        'buttonPressed(' + this.buttonPressed + ')';
    console.log(message);
    document.getElementById('output').innerText = message;
}

var gc = new GameController('/dev/tty.usbmodem1411');