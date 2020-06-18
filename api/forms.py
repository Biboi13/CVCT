from django.forms import ModelForm
from django import forms
from api.models import VCT,Individual,Organization,Prob_occur

class Manage_VCT(ModelForm):
    class Meta:
        model = VCT
        fields = '__all__'
     
class Manage_Individual(ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'

class Manage_Organization(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class Manage_Prob_occur(ModelForm):
    class Meta:
        model = Prob_occur
        fields = '__all__'


