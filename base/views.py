from .models import Product, Student
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# Create Student.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        return Student.objects.create(**validated_data,user=user)

@permission_classes([IsAuthenticated])
class student_Views(APIView):
    
    def get(self, request, pk=-1):  # axios.get
        if pk > -1:
            my_model = Student.objects.get(id=pk)
            serializer = StudentSerializer(my_model, many=False)
        else:
            my_model = request.user.student_set.all()
            serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):  # axios.post
        serializer = StudentSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # axios.put
        my_model = Student.objects.get(pk=pk)
        serializer = StudentSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # axios.delete
        my_model = Student.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['GET','POST'])
    def reg(request):
            print(request)
            User.objects.create_user(
                email=request.data["email"],
                password=request.data["password"],
                username=request.data["username"],
                is_staff=1,is_superuser=0
            )
            return HttpResponse ("register")
    
# Create product.

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def create(self, validated_data):
        prodname = self.context['prodname']
        return Product.objects.create(**validated_data,prodname=prodname)

# @permission_classes([])
class product_Views(APIView):
    
    def get(self, request, pk=-1):  # axios.get
        if pk > -1:
            my_model = Product.objects.get(id=pk)
            serializer = ProductSerializer(my_model, many=False)
        else:
            my_model = request.prodname.Product_set.all()
            serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):  # axios.post
        serializer = ProductSerializer(data=request.data, context={'prodname': request.prodname})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # axios.put
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # axios.delete
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   