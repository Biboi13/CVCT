from rest_framework import serializers
from api.models import VCT,Prob_occur,Individual,Organization

class VCTSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCT
        fields = '__all__'

class Prob_occurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prob_occur
        fields = '__all__'

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
