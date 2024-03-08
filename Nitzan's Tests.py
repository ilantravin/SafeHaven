from django.test import TestCase
from .forms import storyForm

class StoryCreationTest(TestCase):
    def test_create_story_template(self):
        response = self.client.get('/success-story/create-story/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')

    def test_create_story_context(self):
        form = storyForm()
        response = self.client.get('/success-story/create-story/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')
        self.assertEqual(response.context['form'], form)

    def test_create_story_redirect(self):
        response = self.client.post('/success-story/create-story/', data={})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')