import unittest
import api

class TestURLs(unittest.TestCase):
    api = None

    def setUp(self):
        self.api = api.Api('base_url')
        self.api.update_endpoints(
            {
                'a': 'endpoint',
                'b': 'b%(replace)sd',
                'c': None,
                None: 'd'
            }
        )

    def testEndPointCompletion(self):
        expected = 'base_url/endpoint'
        actual = self.api._url('a')
        self.assertEqual(
            actual,
            expected,
            "The basic end point completion did not work"
        )

    def testShouldRaiseNoEndpointFound(self):
        expected = api.EndPointDoesNotExist
        actual = lambda : self.api._url('DNE')
        self.assertRaises(
            expected,
            actual,
        )

    def testURLData(self):
        expected = 'base_url/b3d'
        actual = self.api._url('b', {'replace': 3})
        self.assertEqual(
            actual,
            expected,
            "End Point Completion did not work with URL Data"
        )

    def tearDown(self):
        self.api = None

if __name__ == '__main__':
        unittest.main()
