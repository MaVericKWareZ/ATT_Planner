from rest_framework import serializers

from att_planner.planner.models.bucket import Bucket


class BucketWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bucket
        fields = ('name', 'description')


class BucketReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bucket
        fields = '__all__'
