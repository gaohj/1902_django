from rest_framework import serializers

from App.models import Book


class BookSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ("url","b_name","b_price")

