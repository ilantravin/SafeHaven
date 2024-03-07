import unittest
from django.urls import reverse, resolve
from hosted.views import home, admin


class TestUrls(unittest.TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(url, '/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, home)  # checks if the url pattern resolved to the right view function

    def test_admin_page_url_is_resolved(self):
        url = reverse('admin_page')
        self.assertEqual(url, '/admin_page/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, admin)



