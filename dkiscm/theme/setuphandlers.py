from collective.grok import gs
from dkiscm.theme import MessageFactory as _

@gs.importstep(
    name=u'dkiscm.theme', 
    title=_('dkiscm.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('dkiscm.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
