import unittest
from django.urls import reverse, resolve
from aid_org.views import aid_org

class TestUrls(unittest.TestCase):
    def test_aid_org_url_is_resolved(self):
        url = reverse('aid_org:aid_org')
        self.assertEqual(url, '/aid_org/aid_org/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func,aid_org)  # checks if the url pattern resolved to the right view function