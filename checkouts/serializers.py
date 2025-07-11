from rest_framework import serializers
from .models import Checkout

class CheckoutSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    # queryset None avoiding circular import issues
    book = serializers.PrimaryKeyRelatedField(queryset=None)

    class Meta:
        model = Checkout
        fields = ("id", "user", "book", "checked_out_at", "returned_at")
        read_only_fields = ("checked_out_at", "returned_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # assign queryset for book field dynamically
        from books.models import Book
        self.fields["book"].queryset = Book.objects.all()
