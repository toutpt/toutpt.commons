################################################################
# (C) 2012, ZOPYX Ltd.
################################################################
#ZCML:
#<subscriber handler=".language_negotiation.Negotiator"/>

from zope.interface import Interface
from zope.component import adapter
from ZPublisher.interfaces import IPubEvent,IPubAfterTraversal
from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from zope.app.component.hooks import getSite

@adapter(IPubAfterTraversal)
def Negotiator(event):

    # Keep the current request language (negotiated on portal_languages)
    # untouched

    site = getSite()
    try:
        ms = getToolByName(site, 'portal_membership')
    except AttributeError:
        return
    member = ms.getAuthenticatedMember()
    if member.getUserName() == 'Anonymous User':
        return

    language = member.language
    if language:
        # Fake new language for all authenticated users
        event.request['LANGUAGE'] = language
    else:
        lt = getToolByName(site, 'portal_languages')
        event.request['LANGUAGE'] = lt.getDefaultLanguage()