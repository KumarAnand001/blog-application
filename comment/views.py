from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Comment
from .serializers import CommentSerializer

class CommentView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        
        try:
            post_id = request.data.get('post_id')
            comments = Comment.objects.filter(post=post_id)
            serializer = CommentSerializer(comments, many=True)
            return Response({
                'data': serializer.data,
                'message': 'Comments fetched successfully',
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong while fetching comments',
            }, status=status.HTTP_400_BAD_REQUEST)
        

    def post(self, request):

        try:
            post_id = request.data.get('post_id')
            data = request.data
            data['post'] = post_id
            serializer = CommentSerializer(data=data)

            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response({
                    'data': serializer.data,
                    'message': 'Comment created successfully',
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'data': serializer.errors,
                    'message': 'Failed to create comment',
                }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong while creating comment',
            }, status=status.HTTP_400_BAD_REQUEST)
        