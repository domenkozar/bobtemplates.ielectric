from ...testing import FunctionalTest, BaseUnitTest


class ViewsTests(BaseFunctionalTest):
    def test_index(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue('Hello!' in res.body)


class ViewsTest(BaseUnitTest):
    def test_index(self):
        from ..views import index
        info = index(self.request)
        self.assertEqual(info, {})
