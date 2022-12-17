from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CommentForm
from django.views.generic import View
from django.http import HttpResponseRedirect
from Community.models import Comment


## View for creating a comment and displaying those comments from users
class CommentCreateView(View):
    comment_form_class = CommentForm
    template_name: str = "Community/community_home.html"
    success_url = reverse_lazy("Community:community-home")
    next_page = "Community/community_comment_list.html"

    ## get request for people viewing comments list/box
    def get(self, request):
        comments = Comment.objects.order_by("-create_time")
        comment_form=self.comment_form_class()
        return render(
            request,
            self.template_name,
            {"comment_form": comment_form,"comment_query_set":comments},
        )
    ## Post request when comment is made 
    def post(self, request):
        ## order comments by the creation time so new comments get displayed at the top
        comments = Comment.objects.order_by("-create_time")
        comment_form = self.comment_form_class(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            ## Add a user for the comment
            comment.user = request.user.first_name
            comment.save()
            return HttpResponseRedirect(self.success_url)
        return render(
            request,
            self.template_name,
            {"comment_form":comment_form,"comment_query_set":comments},
        )
