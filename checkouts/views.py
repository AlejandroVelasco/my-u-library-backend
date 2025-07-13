from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Checkout
from .serializers import CheckoutSerializer
from books.models import Book
from users.permissions import IsLibrarian, IsStudent
from rest_framework import serializers
from django.utils import timezone



class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.select_related("user", "book").all()
    serializer_class = CheckoutSerializer

    def get_permissions(self):
        if self.action in ("return_book", "list_all"):
            # only librarians can return books or list all checkouts
            permission_classes = [IsAuthenticated, IsLibrarian]
        else:
            # create (checkout) and list own
            permission_classes = [IsAuthenticated]
        return [p() for p in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.role == "librarian":
            return self.queryset
        # student → only his own checkouts
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        if book.available_copies < 1:
            raise serializers.ValidationError("No copies available")
        # decrease available copies of the book
        book.available_copies -= 1
        book.save()
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"], url_path="return")
    def return_book(self, request, pk=None):
        checkout = self.get_object()
        if checkout.returned_at:
            return Response({"detail": "Already returned"}, status=status.HTTP_400_BAD_REQUEST)
        # set returned_at to now
        checkout.returned_at = timezone.now()
        checkout.save()
        # also increase book available copies
        book = checkout.book
        book.available_copies += 1
        book.save()
        return Response({"detail": "Book returned successfully"})
