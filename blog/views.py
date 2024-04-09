from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, LikeSerializer
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post, Like
from django.db.models import Q

from django.core.paginator import Paginator

class ListPostView(APIView):

    def get(self, request):

        try:

            posts = Post.objects.all().order_by('?')

            if request.GET.get('search'):

                search = request.GET.get('search')
                posts = posts.filter(Q(title__icontains = search) | Q(body__icontains = search))

            page_number = request.GET.get('page', 1)
            paginator = Paginator(posts, 5)

            serializer = PostSerializer(paginator.page(page_number), many = True)

            return Response({

                'data':serializer.data,
                'message':"post fetch successfully",
            }, status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):

        try:

            posts = Post.objects.filter(author = request.user)

            if request.GET.get('search'):

                search = request.GET.get('search')
                posts = posts.filter(Q(title__icontains = search) | Q(body__icontains = search))

            serializer = PostSerializer(posts, many = True)

            return Response({

                'data':serializer.data,
                'message':"post fetch successfully",
            }, status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        try:

            data = request.data
            print(request.user.id)
            data['user'] = request.user.id
            serializer = PostSerializer(data = data)

            print(serializer.is_valid())
            print(serializer.errors)

            if not serializer.is_valid():

                return Response({

                    'data' : serializer.errors,
                    'messege' : 'something went wrong'
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({

                'data' : serializer.data,
                'messege' : 'blog created successfully'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):

        try:

            data = request.data

            post = Post.objects.filter(id = data.get('id'))
            
            if not post.exists():

                return Response({

                    'data' : {},
                    'message': "invalid blog id",
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if request.user != post[0].author:

                return Response({

                    'data' : {},
                    'message':"you are not authrized to this"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = PostSerializer(post[0], data=data, partial = True)

            if not serializer.is_valid():

                return Response({

                    'data' : serializer.errors,
                    'messege' : 'something went wrong'
                }, status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({

                'data': serializer.data,
                'message':'blog updated successfully'
            }, status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):

        try:

            data = request.data

            post = Post.objects.filter(id = data.get('id'))
            
            if not post.exists():

                return Response({

                    'data' : {},
                    'message': "invalid blog id",
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if request.user != post[0].author:

                return Response({

                    'data' : {},
                    'message':"you are not authrized to this"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            post[0].delete()

            return Response({

                'data' : {},
                'message': 'post deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:

            return Response({

                'data' : {},
                'messege' : 'somthing went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


# LikePostView
class LikePostView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        post_id = request.data.get('post_id')
        post = Post.objects.get(pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if created:
            post.likes += 1
            post.save()
            return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

class LikesCountView(APIView):

    def get(self, request):

        post_id = request.data.get('post_id')
        post = Post.objects.get(pk=post_id)
        likes = post.likes
        return Response({'likes': likes}, status=status.HTTP_200_OK)