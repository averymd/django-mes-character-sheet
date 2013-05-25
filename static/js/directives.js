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

});