from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from blog.models import TestModel
# Serializers define the API representation.

class BlogSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_user_methord')
    class Meta:
        model = TestModel
        fields = ['id', 'username', 'slug', 'title', 'content', 'image', 'updated']

    def get_user_methord(self, user_obj):
        username =  user_obj.user.username
        return username