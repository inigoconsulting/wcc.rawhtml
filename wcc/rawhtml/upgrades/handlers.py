from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.rawhtml to 1000',
                description=u'Upgrade wcc.rawhtml to 1000',
                source='1', destination='1000',
                sortkey=1, profile='wcc.rawhtml:default')
def to1000(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.rawhtml.upgrades:to1000')
    catalog = getToolByName(context, 'portal_catalog')
    for brain in catalog(portal_type='wcc.rawhtml.rawhtml'):
        obj = brain.getObject()
        obj.reindexObject()
