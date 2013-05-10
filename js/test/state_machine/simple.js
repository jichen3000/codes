// finite state machine FSM

states = [
    {
        'name':'working',
        'initial':true,
        'events':{
            'bored':'coffee',
            'call_for_meeting':'meeting',
        }
    },
    {
        'name':'coffee',
        'events':{
            'break_over':'working',
            'call_for_meeting':'meeting'
        }
    },
    {
        'name':'meeting',
        'events':{
            'meetings_over':'working'
        }
    },
];

var stateMachine = function (states){
    var indexes = {},
        currentState,
        self = {};
    for( var i = 0; i< states.length; i++){
        indexes[states[i].name] = i;
        if (states[i].initial){
            currentState = states[i];
        }
    }
    self.consumeEvent = function(e){
        if(currentState.events[e]){
            currentState = states[indexes[currentState.events[e]]] ;
        }
    }
    self.getStatus = function(){
        return currentState.name;
    }
    return self;
};

var p = colinM.p;
sm = stateMachine(states);
sm.consumeEvent('bored');
p(sm.getStatus()); // I went for coffee
 
sm.consumeEvent('call_for_meeting');
sm.getStatus(); //will return 'meeting'
 
sm.consumeEvent('bored'); //doesn't matter how boring a meeting can be...
sm.getStatus(); //will still return 'meeting'
 
sm.consumeEvent('meetings_over')
sm.getStatus();  // 'working'