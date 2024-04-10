from django.test import TestCase, Client
from blog.models import Post

from rest_framework import status
from django.contrib.auth.models import User
import json

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test Post', author_id=1, body='This is a test post.')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_author_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_body_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('body').max_length
        self.assertEqual(max_length, 1000)


class ListPostViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_posts(self):
        response = self.client.get('/api/blog/list-post/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_creation(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'New Post', 'body': 'This is a new post.'}
        response = self.client.post('/api/blog/post/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




