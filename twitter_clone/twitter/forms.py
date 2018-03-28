from django.forms import ModelForm

from .models import Tweet


# HINT: Implement TweetForm in order to render input in template and
# validate POSTed data
class TweetForm(ModelForm):
    class Meta:
        pass
