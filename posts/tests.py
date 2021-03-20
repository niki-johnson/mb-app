from django.test import TestCase
from .models import Post
# Create your tests here.

class PostModelTest (TestCase):

    def setUp (self):
        #criando uma nova database que contem a entrada text
        Post.objects.create(text='just a test')

    #primeiro teste
    #checa se a databse realmente contem a str
    def test_text_content (self):
        post = Post.objects.get(id=1)
        #variável para guardar a string contida em post.text
        expected_object_name = f'{post.text}'
        #assert equal verifica se há igualdade com os dois parametroa
        self.assertEqual(expected_object_name,'just a test')

