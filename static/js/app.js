/*globals angular, CharacterSheetListCtrl, CharacterSheetDetailCtrl*/
'use strict';

var m = angular.module('characterSheet', ['characterSheetServices', 'gameServices', 'characterSheetDirectives']);
m.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
    when('/sheets', {templateUrl: 'partials/character-list.html',   controller: CharacterSheetListCtrl}).
    when('/sheets/:id', {templateUrl: 'partials/character-detail.html', controller: CharacterSheetDetailCtrl}).
    when('/sheets/new', {templateUrl: 'partials/character-detail.html', controller: CharacterSheetDetailCtrl}).
    otherwise({redirectTo: '/sheets'});
}]);
  
m.config(function($interpolateProvider) { $interpolateProvider.startSymbol('(('); $interpolateProvider.endSymbol('))'); });