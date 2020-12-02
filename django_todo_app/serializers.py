from rest_framework import serializers
from django_todo_app.models import Tasks, AppUser
from rest_framework.validators import UniqueValidator

class TasksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'text', 'is_completed', 'completed_date', 'author')


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True,
                                    'required': True},
                        'email':    {'required': True}}
        email = serializers.EmailField(
            source='AppUser.email',
            validators=[UniqueValidator(queryset=AppUser.objects.all(), message="email and username should be unique")]
        )


    def create(self, validated_data):
        serializer = AppUserSerializer(data=validated_data)
        serializer.is_valid(raise_exception=True)
        password = validated_data.pop('password')
        print("create" + password)
        user = AppUser(**validated_data)
        user.set_password(password)
        user.save()
        return user