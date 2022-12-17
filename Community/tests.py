from django.test import TestCase
from .forms import CommentForm


## Unit Test(s) for community comment section
class CommentFormTests(TestCase):
    def test_valid(self):
        form = CommentForm(data={"comment":"This is my test comment","user":"averygmp@gmail.com"})
        self.assertEqual(
            form.is_valid(), True
        )
    def test_user_not_email(self):
        form = CommentForm(data={"comment":"This is my test comment","user":"averygmp"})
        self.assertEqual(
            form.errors["user"], ["Enter a valid email address."]
        )
        