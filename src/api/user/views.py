from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfilerSeralizer
from rest_framework.decorators import api_view
from user.models import Profile


@api_view(["GET", "POST"])
def get_users(request):
    if request.method == "GET":
        users = Profile.objects.all()
        result = ProfilerSeralizer(users, many=True).data
        return Response({"data": result})
    elif request.method == "POST":
        serializer = ProfilerSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def get_user(request, pk):
    try:
        user = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response({"error": "Could not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        result = ProfilerSeralizer(user).data
        return Response({"data": result}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProfilerSeralizer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        