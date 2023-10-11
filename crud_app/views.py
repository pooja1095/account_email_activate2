from .models import Project
from .serializers import ProjectModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class ProjectAPI(APIView):

    
    
    def get(self, request):
        obj = Project.objects.all()
        form = ProjectModelSerializer(obj, many=True)
        return Response(data=form.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        form = ProjectModelSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return Response(data=form.data, status=status.HTTP_201_CREATED)
        return Response(data=form.errors, status=status.HTTP_404_NOT_FOUND)
    
class ProjectDetailsAPI(APIView):

    def get(self, request, pk):
        try:
            obj = Project.objects.get(pk=pk)
        except:
            return Response(data={"RecordcNot Found"})
        form = ProjectModelSerializer(instance=obj)
        return Response(data=form.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            obj = Project.objects.get(pk=pk)
        except:
            return Response(data={"message":"Record Not Found"})
        form = ProjectModelSerializer(instance=obj, data=request.data)
        if form.is_valid():
            form.save()
            return Response(data=form.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=form.errors, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            obj = Project.objects.get(pk=pk)
        except:
            return Response(data={"message": "Record Not Found"})
        form = ProjectModelSerializer(instance=obj, data=request.data, partial=True)
        if form.is_valid():
            form.save()
            return Response(data=form.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(data=form.errors, status=status.HTTP_404_NOT_FOUND) 
    
    def delete(self, request, pk):
        try:
            obj = Project.objects.get(pk=pk)
        except:
            return Response(data={"message": "Record Not Found"})
        obj.delete()
        return Response(data={"message":"Record Delete Succesfully"}, status=status.HTTP_200_OK)