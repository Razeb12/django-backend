from rest_framework import serializers
from .models import Profile,Candidate
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','image','number','web','address']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields= ['first_name','last_name','phone','email_address','zip_code','linkedin','resume','writeup','salary_base','salary_bonus','job','pub_date',]
    
    
