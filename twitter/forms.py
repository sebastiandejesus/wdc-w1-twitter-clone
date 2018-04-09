from django import forms


class TweetForm(forms.Form):
    tweet = forms.CharField(
                widget=forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Write your tweet here...',
                        'rows': 2,
                        'cols': 11,
                    }
                )
            )
