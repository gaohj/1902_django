from rest_framework import serializers

from App.models import Book,Game,Movie,User


class BookSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ("url","b_name","b_price")


class Book1Serializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id","b_name","b_price")


class Book2Serializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    b_name = serializers.CharField()
    b_price = serializers.FloatField()
    def update(self, instance, validated_data):
        instance.b_name = validated_data.get('b_name') or instance.b_name
        instance.b_price = validated_data.get('b_price') or instance.b_price
        instance.save()

        return instance
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class GameSerializers(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ("id","g_name","g_price")

class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id","m_name","m_price")


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id","u_name","u_password")