from rest_framework import serializers
from .models import Checkout
from books.models import Book

class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Checkout
        fields = ("id", "user", "book", "checked_out_at", "returned_at")
        read_only_fields = ("checked_out_at", "returned_at")

