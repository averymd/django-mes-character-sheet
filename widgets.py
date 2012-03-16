from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django import forms
from game_manager.models import Trait

class DotRenderer(forms.widgets.RadioFieldRenderer):
    """ Modifies some of the Radio buttons to be disabled in HTML,
    based on an externally-appended Actives list. """

    def render(self):
        if not hasattr(self, "actives"): # oops, forgot to add an Actives list
            return self.original_render()
        return self.my_render()

    def original_render(self):
        return mark_safe(u'<ul>\n%s\n</ul>' % u'\n'.join([u'<li>%s</li>'
            % force_unicode(w) for w in self]))

    def my_render(self):
      midList = []
      print 'in my_render'
      print 'renderer choices'
      print self.choices
      for x, wid in enumerate(self):
        if not self.actives[x]:
          wid.attrs['disabled'] = True
        midList.append(u'<li>%s</li>' % force_unicode(wid))
      finalList = mark_safe(u'<ul>\n%s\n</ul>' % u'\n'.join([u'<li>%s</li>'
        % w for w in midList]))
      self.actives = [True for i in range (0, 5)]
      return finalList