from django.test import TestCase, Client
from django.urls import reverse
from success_story.models import story


class TestViews(TestCase):
    def setup(self):
        self.client = Client()
        self.create_story_url = reverse('success_story:create_story')
        self.obj = story.objects.create(date='2022-2-2',
                                        name='test',
                                        text='testing')

    def test_all_stories_GET(self):
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')

    def test_create_story_GET(self):
        response = self.client.get(reverse('success_story:create_story'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')

    def test_create_story_POST_valid(self):
        response = self.client.post(reverse('success_story:create_story'), {'date': '2021-11-10',
                                                                      'name': 'test',
                                                                      'text': 'testing'})
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/success_story/all_stories/')

    def test_create_story_POST_Not_valid(self):
        response = self.client.post(reverse('success_story:create_story'), {'date': '2021-11-10',
                                                                            'name': '',  # fail here
                                                                            'text': 'testing'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')

