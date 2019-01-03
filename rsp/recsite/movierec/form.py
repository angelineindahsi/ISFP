from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'user_name','comment']
        widgets = {
        'comment': Textarea(attrs={'cols': 35, 'rows': 10})
        }




