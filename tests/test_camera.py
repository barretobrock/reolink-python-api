import unittest
from reolink_api import Camera
from tests.common import make_patcher


class TestCamera(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        # Mock requests so these. tests don't touch external systems
        self.mock_requests = make_patcher(self, 'reolink_api.resthandle.requests')
        # Prime responses
        self.mock_requests.post.return_value.status_code = 200
        self.mock_requests.post.return_value.json.return_value = [
            {
                'code': '0',
                'value': {
                    'Token': {
                        'name': 'somekindoftoken'
                    }
                }
            }
        ]

        self.ip = '0.0.0.1'
        self.un = 'someuser'
        self.pw = 'somepw'
        self.cam = Camera(ip=self.ip, username=self.un, password=self.pw)

    def test_camera(self):
        """Test that camera connects and gets a token"""
        self.assertTrue(self.cam.ip == self.ip)
        self.assertTrue(self.cam.token != '')
        self.mock_requests.post.assert_called()


if __name__ == '__main__':
    unittest.main()
