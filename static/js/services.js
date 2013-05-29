angular.module('characterSheetServices', ['ngResource']).factory('CharacterSheet', function($resource){
  var Sheet = $resource('https://api.mongolab.com/api/1/databases/devcharactermanager/collections/charactersheets/:id', 
    { apiKey:'0MYTa3INCIuUL9-VD-lrEoPPsuXgKBEP' },
    { update: {method: 'PUT'} }
  );
  
  Sheet.getById = function (id, cb, errorcb) {
    return Sheet.get({id:id}, cb, errorcb);
  }; 
  
  Sheet.prototype.update = function(cb) {
    return Sheet.update({id: this._id.$oid},
      angular.extend({}, this, {_id:undefined}), cb);
  };
  
  Sheet.prototype.saveOrUpdate = function (savecb, updatecb, errorSavecb, errorUpdatecb) {
    if (this._id && this._id.$oid) {
      return this.update(updatecb, errorUpdatecb);
    } else {
      return this.$save(savecb, errorSavecb);
    }
  };
  
  Sheet.prototype.remove = function (cb, errorcb) {
      return Sheet.remove({id:this._id.$oid}, cb, errorcb);
    };

  Sheet.prototype.destroy = function(cb) {
    return Sheet.remove({id: this._id.$oid}, cb);
  };  
  
  Sheet.create = function(cb) {
    var character = angular.extend({}, this, this.prototype, {_id:undefined, attributes:{}, skills:{}, merits:{}});
    if (typeof (cb) === 'function')
      cb(character);
    return character;
  };

  return Sheet;
});

angular.module('gameServices', ['ngResource']).
  factory('Faction', function($resource){
    return $resource('/game-manager/factions/:game_id\\/', {}, {
      query: { method: 'GET', params: { game_id: '1' }, isArray: true }
    });
  }).
  factory('Game', function($resource){
    return $resource('/game-manager/games/:game_name/:game_id\\/', {}, {
      query: { method: 'GET', params: { game_id: '1', game_name: 'geist' }, isArray: false }
    });
  }).
  factory('Subrace', function($resource){
    return $resource('/game-manager/subraces/:game_id\\/', {}, {
      query: { method: 'GET', params: { game_id: '1' }, isArray: true }
    });
  });