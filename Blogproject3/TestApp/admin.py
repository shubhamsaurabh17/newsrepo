from django.contrib import admin
from TestApp.models import Post, Comment, Feedback, Breaking
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=["title","slug","author","created","publish","status","body"]
    list_filter=("status","publish","author")
    raw_id_fields=('author',)
    ordering=['status','publish']


class CommentAdmin(admin.ModelAdmin):
    list_display=["name","email","created","active","post","body"]
    list_filter=("active","created","updated")
    search_fields=("name","email","body")


class FeedbackAdmin(admin.ModelAdmin):
    list_display=["name","email","feedback"]

class BreakingAdmin(admin.ModelAdmin):
    list_display=["body"]

admin.site.register(Breaking,BreakingAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
