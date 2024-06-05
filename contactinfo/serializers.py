from rest_framework import serializers
from .models import ContactInfo

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            'id', 'name', 'email', 'phone_number_one', 'phone_number_two',
            'address', 'facebook_link', 'instagram_link', 'linkedin_link', 'youtube_link'
        ]