from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer
from .permissions import IsLibrarian
from rest_framework.decorators import api_view, permission_classes

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = "username"

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ("create", "list", "retrieve"):
            # only authenticated users, also only librarians can list or retrieve users
            permission_classes = [IsAuthenticated, IsLibrarian]
        else:
            # also only authenticated librarians can update or delete users
            permission_classes = [IsAuthenticated, IsLibrarian]
        return [p() for p in permission_classes]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    # returns full user data, including role
    return Response(UserSerializer(request.user).data)