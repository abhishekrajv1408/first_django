# from attr import field
from django.forms import ModelForm
from .models import Details

class UserForm(ModelForm):
    class Meta:
        model=Details
        fields=[
            'name',
            'age',
        ]