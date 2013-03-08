from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from five import grok
from collective.grok import gs
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('wcc.rawhtml')

_ = MessageFactory

class HiddenProducts(grok.GlobalUtility):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)
    grok.name('wcc.rawhtml.upgrades')

    def getNonInstallableProducts(self):
        return [
            'wcc.rawhtml.upgrades',
        ]

gs.profile(name=u'default',
           title=u'wcc.rawhtml',
           description=_(u''),
           directory='profiles/default')
