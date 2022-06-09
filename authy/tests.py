from django.test import TestCase
from authy.models import Profile

# Create your tests here.
class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='neal')
        self.profile = Profile.objects.create(user = self.user,bio = 'dnd')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_create_user_profile(self):
        self.assertTrue(isinstance(self.profile, Profile))