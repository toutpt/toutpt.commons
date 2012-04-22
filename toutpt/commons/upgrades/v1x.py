from Products.CMFCore.utils import getToolByName

def upgrade_1000_to_1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-toutpt.commons:default',
                                   "browserlayer")
    setup.runAllImportStepsFromProfile('profile-collective.ckeditor:default')

def upgrade_1001_to_1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile('profile-toutpt.commons:default',
                                   "propertiestool")
