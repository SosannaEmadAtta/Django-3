from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'email', 'password', 'image']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #  Override the create method to hash the password
    def create(self, validated_data):
        account = Account.objects.create(**validated_data)
        return account
