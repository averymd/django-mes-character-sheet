function CharacterSheetListCtrl($scope, CharacterSheet) {
  $scope.characters = CharacterSheet.query();
  $scope.orderProp = 'name';
}

function CharacterSheetDetailCtrl($scope, $routeParams, $location, CharacterSheet, Faction, Subrace, Game) {
  var getGameInformation = function(returnedCharacter) {
    if (typeof (returnedCharacter.game_id) == 'undefined') {
      returnedCharacter.game_id = 1;
      returnedCharacter.game_name = 'geist';
    }
    $scope.factions = Faction.query({game_id: returnedCharacter.game_id});
    $scope.subraces = Subrace.query({game_id: returnedCharacter.game_id});
    $scope.game = Game.get({game_name: returnedCharacter.game_name, game_id: returnedCharacter.game_id});
  };
  if ($routeParams.id != 'new') {
    $scope.character = CharacterSheet.getById($routeParams.id, getGameInformation);
  } else {
    $scope.character = CharacterSheet.create(getGameInformation);
  }
  //getGameInformation();
  
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
  
  $scope.availableDots = function(dotList) {
    if (dotList === '')
      return $scope.scale;
    else
      return dotList.split(',');
  };
  
  var redirectToCharacterById = function(returnedCharacter) {
    if ($routeParams.id != returnedCharacter._id.$oid) {
      $location.path('/sheets/' + returnedCharacter._id.$oid);
    }
  };
}

//CharacterSheetDetailCtrl.$inject = ['$scope', '$routeParams', 'CharacterSheet'];