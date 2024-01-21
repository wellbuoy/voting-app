from django.contrib import admin

# Import the Post, Question and Choice model from the models module in the current directory
from .models import Post

# Register the Post model with the admin site
admin.site.register(Post)
