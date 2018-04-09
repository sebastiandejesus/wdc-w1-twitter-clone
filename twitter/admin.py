from django.contrib import admin
from twitter.models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    fields = ['username', 'post_date', 'tweet']
