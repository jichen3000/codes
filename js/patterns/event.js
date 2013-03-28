var publisher = {
    subscribe: function (name, type, fun) {
        this.subscribers = this.subscribers || [];
        this.subscribers.push({
            'name': name,
            'type': type,
            'fun': fun
        });
    },
    publish: function (type) {
        for (var i = this.subscribers.length - 1; i >= 0; i--) {
            this.subscribers[i]
        };
        for (var i = this.subscribers.length - 1; i >= 0; i--) {
            if(this.subscribers[i]['type']===type){
                this.subscribers[i]['fun'].apply(this, 
                    Array.prototype.slice.call(arguments, 1));
            }
        };
    }
};

var daily_post = {
    subscribers: [],
    morning_delivery: function () {
        this.publish('daily_post');
    }
};

var copy_funs = function (target, source) {
    for(variable in source){
        if(source.hasOwnProperty(variable) && typeof source[variable] === 'function'){
            target[variable] = source[variable];
        }
    }
};

copy_funs(daily_post, publisher);
daily_post.subscribe('colin', 'daily_post', function () {
    console.log("Colin receive the daily_post");
});

daily_post.morning_delivery();





