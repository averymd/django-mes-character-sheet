CharonSheet.character = DS.Model.extend({
	name: DS.attr('string'),
	concept: DS.attr('string'),
  age: DS.attr('string'),
  dob: DS.attr('string'), //Make this a date?
  virtue: DS.attr('number'), //TODO: Replace this with a connection to the game's virtue array!
  vice: DS.attr('number'), //TODO: Replace this with a connection to the game's virtue array!
  mc_level_at_creation: DS.attr('number')
})

CharonSheet.character.FIXTURES = [
{
	id: 0,
	name: 'Archibald Fortinbras Barrayan',
	concept: 'Dead socialite',
	age: '30',
	dob: '1/1/1983',
	virtue: 1,
	vice: 1,
	mc_level_at_creation: 1
}
]