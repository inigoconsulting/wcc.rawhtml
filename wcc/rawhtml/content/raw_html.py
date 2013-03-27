from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.rawhtml import MessageFactory as _


# Interface class; used to define content-type schema.

class IRawHTML(form.Schema, IImageScaleTraversable):
    """
    A raw html content type
    """
    raw_html = schema.Text(title=u'HTML Code', required=True)
    type_tag = schema.TextLine(title=u'Meta type', required=False)
    wrap_plone = schema.Bool(
        title=_(u'Wrap with Plone theme'),
        required=False,
        default=False,
    )
