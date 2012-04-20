from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class Layer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import toutpt.commons
        self.loadZCML(package=toutpt.commons)

        # Install product and call its initialize() function
        z2.installProduct(app, 'toutpt.commons')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'toutpt.commons:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'toutpt.commons')

FIXTURE = Layer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="toutpt.commons:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="toutpt.commons:Functional")
