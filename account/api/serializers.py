from rest_framework import serializers
from django.contrib.auth.models import User
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def save(self):
        user_obj = User.objects.create_user(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "email", "username"]