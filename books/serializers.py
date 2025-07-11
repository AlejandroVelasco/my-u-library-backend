from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "published_year",
            "genre",
            "total_copies",
            "available_copies",
        )
        read_only_fields = ("available_copies",)
