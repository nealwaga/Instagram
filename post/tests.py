from django.test import TestCase
from post.models import Post

# Create your tests here.
class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='neal')
        self.profile = Profile.objects.create(user = self.user,bio = 'dnd')

        self.image = Post.objects.create(posted_by = self.user,
                                          profile = self.profile,
                                          caption ='lifestyle',
                                          likes = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Post))

    def test_get_absolute_url(self):
        self.image.save()
        image = Post.get_images()
        self.assertTrue(len(image) == 1)