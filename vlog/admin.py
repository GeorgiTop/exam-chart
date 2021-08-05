from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import VlogPost


class AdminVlogPost(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(VlogPost, AdminVlogPost)
