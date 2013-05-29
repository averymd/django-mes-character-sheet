angular.module('characterSheetDirectives', []).
directive('ensureExistence', function() {
  return {
    restrict: 'A',
    scope: {
      ensureExistence: '='
    },
    link: function(scope, element, attrs) {
      if (typeof (scope.ensureExistence) === 'undefined')
        scope.ensureExistence = {};
    }
  };
}).
directive('xpSelector', function() {
  return {
    restrict: 'A',
    require: 'ngModel',
    link: function(scope, element, attrs, ngModel) {
      scope.$watch(attrs.ngModel, function(newVal, oldVal) {
        console.log('old value: ' + oldVal + ' and new val: ' + newVal);
        
        if (oldVal != newVal) {
          var xpCost = 0;
          if (attrs.trait.uses_simple_calculation) {
            if (attrs.trait.custom_xp_per_dot) {
              if (oldVal < newVal) {
                xpCost = newVal * attrs.trait.custom_xp_per_dot;
              } else {
                xpCost = (newVal - oldVal) * attrs.trait.custom_xp_per_dot;
              }
            } else {
              if (oldVal < newVal) {
                xpCost = newVal * attrs.trait.trait_type.default_xp_cost_per_dot;
              } else {
                xpCost = (newVal - oldVal) * attrs.trait.trait_type.default_xp_cost_per_dot;
              }
            } 
          } else {
            if (attrs.trait.custom_xp_per_dot) {
              if (oldVal < newVal) {
                for (var i = oldVal + 1; i <= newVal; i++) {
                  xpCost = xpCost + i * attrs.trait.custom_xp_per_dot;
                }
              } else {
                for (var i = newVal + 1; i <= oldVal; i++) {
                  xpCost = xpCost + i * attrs.trait.custom_xp_per_dot;
                }
                xpCost = -1*xpCost;
              }
            } else {
              if (oldVal < newVal) {
                for (var i = oldVal + 1; i <= newVal; i++) {
                  xpCost = xpCost + i * attrs.trait.trait_type.default_xp_cost_per_dot;
                }
              } else {
                for (var i = newVal + 1; i <= oldVal; i++) {
                  xpCost = xpCost + i * attrs.trait.trait_type.default_xp_cost_per_dot;
                }
                xpCost = -1*xpCost;
              }
            }
          }
        
          xpCost = xpCost * -1;
          
          var description = xpCost + ' XP on ' + attrs.trait.name;
          var category = 0;
          
          for (var i = 0; i < scope.game.xp_category_options.length; i++) {
            if (scope.game.xp_category_options[i][1].toLowerCase() == attrs.trait.trait_type.name.toLowerCase()) {
              category = scope.game.xp_category_options[i][0];
              break;
            }
          }
          if (typeof (scope.character.xp_logs) == 'undefined') {
            scope.character.xp_logs = [];
          }
          scope.character.xp_logs.push({
            date: new Date(),
            category: category,
            xp_change: xpCost,
            details: description,
            trait_id: attrs.trait.id
          });
        }
      });
    }
  };
});