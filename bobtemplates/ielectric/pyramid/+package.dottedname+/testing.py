import unittest2 as unittest
import mock

from pyramid import testing


class BaseUnitTest(unittest.TestCase):
    mock = mock

    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)

    def tearDown(self):
        testing.tearDown()


class BaseIntegrationTest(BaseUnitTest):
    include_apps = []

    def setUp(self):
        super(BaseIntegrationTest, self).setUp()
        for app in self.include_apps:
            self.config.include(app)


class BaseFunctionalTests(unittest.TestCase):
    mock = mock

    def setUp(self):
        from webtest import TestApp
        from . import main
        app = main({})
        self.testapp = TestApp(app)
        # TODO: SQL functional testing
