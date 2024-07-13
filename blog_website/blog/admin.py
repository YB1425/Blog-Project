from django.contrib import admin
from .models import UserTable
from .models import PostTable
from .models import PostCategory
from .models import Comment

admin.site.register(UserTable)
admin.site.register(PostTable)
admin.site.register(PostCategory)
admin.site.register(Comment)

