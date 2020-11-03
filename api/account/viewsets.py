from users.models import Customer, Employee
# from rest_framework.permissions import  isAuthenticatedOrReadOnly
from .permissions import IsOwnerOrIsStaffOrReadOnly
from rest_framework import  viewsets
from .serializers import UserCreateSerializer,CustomerSerializer ,EmployeeSerializer
# from rest_framework.filters import  SearchFilter,OrderingFilter 
from django.contrib.auth import get_user_model

User = get_user_model()                


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all() 

# TODO: generics.RetrieveUpdateDestroyAPIView instead of ModelViewSet
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsOwnerOrIsStaffOrReadOnly]
    queryset = Customer.objects.all() 

# TODO: generics.RetrieveUpdateDestroyAPIView instead of ModelViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsOwnerOrIsStaffOrReadOnly]
    queryset = Employee.objects.all() 
    
   
   
