from django.test import TestCase
from django.urls import reverse

from.models import story


class AllStoriesTests(TestCase):
    def test_all_stories_template(self):
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')

    def test_all_stories_context(self):
        stories = story.objects.all()
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')
        self.assertEqual(response.context['stories'], stories)

    def test_all_stories_url(self):
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')

    def test_all_stories_form(self):
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')
        form = response.context['form']
        self.assertIsInstance(form, storyForm)

    def test_all_stories_view(self):
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')
        self.assertEqual(response.context['view'].kwargs['pk'], None)