from django.urls import reverse
from django.test import TestCase, Client
from aid_org.models import AidOrg

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.aid_org_url = reverse('aid_org:aid_org')
        self.aid_org = AidOrg.objects.create(
            name='Test Aid Org',
            description='Test Description',
            website='www.test.com',
            #logo='default.jpg'
        )