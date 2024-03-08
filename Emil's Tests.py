from django.test import TestCase
from django.urls import reverse

from.models import aid_org
from.forms import AidOrgForm


class AidOrgTests(TestCase):
    def test_aid_org_creation(self):
        aid_org1 = aid_org.objects.create(name='Test Aid Org')
        self.assertEqual(aid_org1.name, 'Test Aid Org')

    def test_aid_org_view(self):
        response = self.client.get(reverse('aid_org'))
        self.assertEqual(response.status_code, 200)

    def test_aid_org_url_resolves(self):
        resolver = resolve('/aid_org/')
        self.assertEqual(resolver.view_name, 'aid_org')

    def test_aid_org_form_valid(self):
        form = AidOrgForm(data={'name': 'Test Aid Org'})
        self.assertTrue(form.is_valid())