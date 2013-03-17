var events = require('events');

var eventEmitter = new events.EventEmitter();

eventEmitter.on('someOccurence', function(message){
    console.log('before %s', message);
});
eventEmitter.on('someOccurence', function(message){
    console.log(message);
});
eventEmitter.on('someOccurence', function(message){
    console.log('after %s', message);
});

eventEmitter.emit('someOccurence', 'Something happened!');