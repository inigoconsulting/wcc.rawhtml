from five import grok
from plone.directives import dexterity, form
from wcc.rawhtml.content.raw_html import IRawHTML

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IRawHTML)
    grok.require('zope2.View')
    grok.template('raw_html_view')
    grok.name('view')

