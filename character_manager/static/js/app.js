CharonSheet = Ember.Application.create({
  LOG_TRANSITIONS: true
});

CharonSheet.Router.map(function() {
  this.resource('tabletop', { path: '/'});
});

CharonSheet.virtues = ['Charity', 'Faith', 'Fortitude', 'Hope', 'Justice', 'Prudence', 'Temperance']; //TODO: Take these from Game and keep them in the model?
CharonSheet.vices = ['Charity', 'Faith', 'Fortitude', 'Hope', 'Justice', 'Prudence', 'Temperance']; //TODO: Take these from Game and keep them in the model?

CharonSheet.skills = {
	mental: ['Academics', 'Computer', 'Crafts', 'Investigation', 'Medicine', 'Occult', 'Politics', 'Science'],
	physical: ['Athletics', 'Brawl', 'Drive', 'Firearms', 'Larceny', 'Stealth', 'Survival', 'Weaponry'],
	social: ['Animal Ken', 'Empathy', 'Expression', 'Intimidation', 'Persuasion', 'Socialize', 'Streetwise', 'Subterfuge']
};

CharonSheet.TabletopRoute = Ember.Route.extend({
  model: function () {
    return CharonSheet.character.find();
  }
});

CharonSheet.TraitView = Ember.View.extend({
	templateName: 'trait',
	idPrefix: function(){
		console.info(this.get("trait").toLowerCase().replace(" ",""));
		return this.get("trait").toLowerCase().replace(" ",""); //We'll wanna replace this with the trait's actual ID.
	}.property('trait')
});

Ember.Handlebars.registerBoundHelper('dots', function() {
	var ret = '';
	var n = arguments[1] || 5;

	for(var i=1; i<=n; i++)
	{
		ret += '<input type="checkbox" id="' + arguments[0] + '-attr-'+ i + '"/><label for="' + arguments[0] +'-attr-'+ i + '"></label>';
	}
	return new Handlebars.SafeString(ret);
});