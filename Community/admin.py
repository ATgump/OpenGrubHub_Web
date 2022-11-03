from django.contrib import admin
from .models import Comment



# ### THis is to update what admin can see in the users
# class CommentInline(admin.StackedInline):
#     model = Comment
#     can_delete = True
#     verbose_name_plural = "Comments"
#     fk_name = "user"
# class CommentAdmin(admin.ModelAdmin):
#     inlines = (
#         CommentInline,
#     )
#     list_display = (
#         "get_comment",
#         "get_user",

#     )
#     def get_comment(self, instance):
#         return instance.comment
    
#     get_comment.short_description = "Comment"

#     def get_user(self, instance):
#         return instance.user
#     get_user.short_description = "User"
    
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CommentAdmin, self).get_inline_instances(request, obj)


admin.site.register(Comment)
# admin.site.register(User, CustomUserAdmin)
