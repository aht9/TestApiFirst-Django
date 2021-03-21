from rest_framework import serializers
from .models import ShowTodo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowTodo
        fields = ('id', 'Title', 'Description', 'DoItCheck', 'UserCreated', 'On_Created', 'Image', 'SignatureImage', 'On_Updated')
