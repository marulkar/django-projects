from django import forms
from models import Projects


class ProjectViewForm(forms.ModelForm):  

    class Meta:
        model = Projects
        fields = ('title', 'body', 'technologies_used', 'pub_date')


