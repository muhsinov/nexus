from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from product.models import Product, ProductImage, ProductView

@api_view(["GET", "POST"])
def get_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        result = ProductSerializer(products, many=True).data
        return Response({"data": result}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Could not found"})

    if request.method == "GET":
        result = ProductSerializer(product).data
        return Response({"data": result}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    