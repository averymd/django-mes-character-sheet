function CharacterSheetListCtrl($scope, CharacterSheet) {
  $scope.characters = CharacterSheet.query();
  $scope.orderProp = 'name';
}

function CharacterSheetDetailCtrl($scope, $routeParams, $location, CharacterSheet, Faction, Subrace, Game) {
  var getGameInformation = function() {
    if (typeof ($scope.character.game_id) == 'undefined') {
      $scope.character.game_id = 1;
      $scope.character.game_name = 'geist';
    }
    $scope.factions = Faction.query({game_id: $scope.character.game_id});
    $scope.subraces = Subrace.query({game_id: $scope.character.game_id});
    $scope.game = Game.get({game_name: $scope.character.game_name, game_id: $scope.character.game_id});
  };
  if ($routeParams.id != 'new') {
    $scope.character = CharacterSheet.getById($routeParams.id);
  } else {
    $scope.character = CharacterSheet.create();
  }
  getGameInformation();
  
  $scope.vices = [
    { id: '1', name: 'Envy' },
    { id: '2', name: 'Gluttony' },
    { id: '3', name: 'Greed' },
    { id: '4', name: 'Lust' },
    { id: '5', name: 'Pride' },
    { id: '6', name: 'Sloth' },
    { id: '7', name: 'Wrath' }
  ];
  $scope.virtues = [
    { id: '1', name: 'Charity' },
    { id: '2', name: 'Faith' },
    { id: '3', name: 'Fortitude' },
    { id: '4', name: 'Hope' },
    { id: '5', name: 'Justice' },
    { id: '6', name: 'Prudence' },
    { id: '7', name: 'Temperance' }
  ];
  $scope.scale = [1,2,3,4,5];
  
  $scope.save = function() {
    $scope.character.saveOrUpdate(redirectToCharacterById);    
    //$scope.cancel();
  }
  
  $scope.saveAndReturn = function() {
    $scope.character.saveOrUpdate();
    $location.path('/sheets');
    //$scope.cancel();
  }
  
  var redirectToCharacterById = function(returnedCharacter) {
    if ($routeParams.id != returnedCharacter._id.$oid) {
      $location.path('/sheets/' + returnedCharacter._id.$oid);
    }
  };
}

//CharacterSheetDetailCtrl.$inject = ['$scope', '$routeParams', 'CharacterSheet'];