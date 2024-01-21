from django.db import models

class Post(models.Model):

    # Represents a title for the post
    title = models.CharField(max_length=140)

    # Contains the body text of the post
    body = models.TextField()

    # Records the date and time when the post was created
    date = models.DateTimeField(auto_now_add=True)

    # Holds an optional signature for the post
    signature = models.CharField(max_length=140, default='Maxwell')
    
    # Sorts the posts in descending order based on the date they were created
    class Meta:
        ordering = ['-date']


