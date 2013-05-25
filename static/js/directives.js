angular.module('characterSheetDirectives', []).
directive('dotSelector', function() {
  return {
    template: '<label class="radio inline"><input type="radio" value="0">None</label>' +
      '<label class="radio inline"><input type="radio" value="1">1</label>' +
      '<label class="radio inline"><input type="radio" value="2">2</label>' +
      '<label class="radio inline"><input type="radio" value="3">3</label>' +
      '<label class="radio inline"><input type="radio" value="4">4</label>' +
      '<label class="radio inline"><input type="radio" value="5">5</label>',
    replace: true,
    require: '?ngModel',
    link: function(scope, element, attrs, ngModel) {
      element.find('input').bind('click', function(elem) {
        ngModel.$setViewValue(elem.val());
      });
    }
  };

});