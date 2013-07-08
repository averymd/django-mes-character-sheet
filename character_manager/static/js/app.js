CharonSheet = Ember.Application.create({
  LOG_TRANSITIONS: true
});

CharonSheet.Router.map(function() {
  this.resource('tabletop', { path: '/'
});
});

CharonSheet.TabletopRoute = Ember.Route.extend({
  model: function () {
    return CharonSheet.character.find();
  }
});