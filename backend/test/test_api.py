import unittest
import pytest
import os

from apiservice import userapiservice

class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.service = userapiservice.UserAPiService()
        return super().setUp()
    
    def test_octacat_user_gists(self):
        response=self.service.processusergists("choco", 1)
        self.assertEqual(response['status_code'], 200)
        
    def test_octacat_user_gists_fail(self):
        os.environ["token"]="wrong_token"
        self.assertNotEqual(self.service.processusergists("octacat",1)['error_message'], 200)