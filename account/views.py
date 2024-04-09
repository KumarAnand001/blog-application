from ast import Return
from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status

from django.shortcuts import render

class RegisterView(APIView):

  
    def post(self, request):

        try:

            data = request.data
            serializer = RegisterSerializer(data = data)
            if not serializer.is_valid():

                return Response({

                    'data' : serializer.errors,
                    'messege' : 'something went wrong'
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({

                'data' : {},
                'messege' : 'your account is created'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Your account has been created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):

        try:

            data = request.data
            serializer = LoginSerializer(data = data)
            if not serializer.is_valid():

                return Response({

                    'data' : serializer.errors,
                    'messege' : 'something went wrong'
                }, status= status.HTTP_400_BAD_REQUEST)
            
            response = serializer.get_jwt_token(serializer.data)
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

