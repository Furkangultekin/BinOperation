from rest_framework import serializers
from .models import Bin, BinOperation, Operation


# Bin Serializer
class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ['bin_id', 'latitude', 'longitude']

    # Create a new bin
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['operation_id', 'name']

    # Create a new Operation
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class BinOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinOperation
        fields = ['bin', 'operation', 'collection_frequency', 'last_collection']

    # Create a new bin-operation pair
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
