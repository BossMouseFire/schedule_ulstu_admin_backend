from rest_framework import serializers
from ..models import BotUsers, BotSchedulePictures, BotScheduleUlSTU, FacultiesULSTU


class BotUsersSerializers(serializers.ModelSerializer):

    class Meta:
        model = BotUsers
        fields = '__all__'


class BotSchedulePicturesSerializers(serializers.ModelSerializer):

    class Meta:
        model = BotSchedulePictures
        fields = '__all__'


class BotScheduleUlSTUSerializers(serializers.ModelSerializer):

    class Meta:
        model = BotScheduleUlSTU
        fields = '__all__'


class FacultiesULSTUSerializers(serializers.ModelSerializer):

    class Meta:
        model = FacultiesULSTU
        fields = '__all__'


class BotUsersRetrieveSerializers(serializers.ModelSerializer):
    faculty = FacultiesULSTUSerializers()

    class Meta:
        model = BotUsers
        fields = '__all__'
