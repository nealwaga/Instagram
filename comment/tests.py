from django.test import TestCase
from comment.models import Comment

# Create your tests here.
class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='neal')

        self.comment= Comment.objects.create(poster= self.user, comment='new comment' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_user_comment_post(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_user_del_comment_post(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)