from collective.grok import gs
from wcc.rawhtml import MessageFactory as _

@gs.importstep(
    name=u'wcc.rawhtml', 
    title=_('wcc.rawhtml import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.rawhtml.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
