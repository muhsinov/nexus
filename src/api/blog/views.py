from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from blog.models import Post
from .serializers import BlogSerializers

class BlogGenericAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializers
    
    
    def get(self, request):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": "invalid"}, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailGenericAPIView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializers
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
    




# class BlogGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = BlogSerializers
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class BlogDetailGenericAPIView(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = BlogSerializers
#     lookup_field = "pk"
    
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
        
            