from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from rest_framework.decorators import action
from .permissions import IsAdminUserRole


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUserRole])
    def update_role(self, request, pk=None):
        user = self.get_object()
        new_role = request.data.get('role')
        if new_role not in ['customer', 'admin']:
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)
        user.role = new_role
        user.save()
        return Response({"message": f"Role updated to {new_role}"})


