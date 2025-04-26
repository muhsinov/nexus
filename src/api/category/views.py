from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from category.models import Category


@api_view(['GET', 'POST'])
def get_category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True).data
        return Response({"data": result})
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(["GET", "PUT", "DELETE"])
def ctg_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        result = CategorySerializer(category).data
        return Response({"data": result}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)