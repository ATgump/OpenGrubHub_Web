from django import forms
from Community.models import Comment


## Form for a user comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment","user",)
        widgets = {
            "user":forms.HiddenInput(),
            "comment":forms.Textarea(attrs={'rows':5, 'cols':20}) 
        }
