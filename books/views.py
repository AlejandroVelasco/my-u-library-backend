from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from users.permissions import IsLibrarian

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author", "genre"]

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            # only librarians can create, update, or delete books
            permission_classes = [IsAuthenticated, IsLibrarian]
        else:
            # list, retrieve: any authenticated user
            permission_classes = [IsAuthenticated]
        return [p() for p in permission_classes]
