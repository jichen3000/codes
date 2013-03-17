// It is the model.
var Status = Backbone.Model.extend({
  url: '/status',
  validate: function(attrs){
    return "error: "+attrs.text;
  }
});

// It is the controller.
var Statuses = Backbone.Collection.extend({
  model: Status
});


// It is the view
var NewStatusView = Backbone.View.extend({
  events: {
    'submit form': 'addStatus'
  },
  initialize: function(){
    this.collection.on('add', this.clearInput, this);  
  },
  addStatus: function(e){
    e.preventDefault();
    
    // it will trige the 'add' method on collection    
    this.collection.create({text:this.$('textarea').val()});
  },
  clearInput: function(){
    this.$('textarea').val('');
  }
});

//As each view is now responsible for only one HTML element
var StatuesView = Backbone.View.extend({
  initialize: function(){
    this.collection.on('add', this.appendStatus, this);
    this.collection.on('error', this.appendError, this);
  },
  appendStatus: function(status){
    this.$('ul').append('<li>' + status.escape('text') + '</li>');
  },
  appendError: function(model, error){
    //  alert(error);
    this.$('ul').append('<li>' + error + '</li>');
  }
});

$(document).ready(function() {
  var statuses = new Statuses();
  new NewStatusView({collection : statuses, el:$('#new-status')});
  new StatuesView({collection : statuses, el:$('#statuses')});
});




