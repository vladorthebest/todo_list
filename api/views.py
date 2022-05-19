from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import *
from .serializers import TaskSerializers


@api_view(['GET'])
def getTasks(request):
    #dict with tasks
    tasks = Task.objects.all()[::-1]
    serialazer = TaskSerializers(tasks, many=True)

    return Response(serialazer.data)


@api_view(['POST'])
def addTask(request):
    serialazer = TaskSerializers(data=request.data)
    if serialazer.is_valid():
        serialazer.save()
        
    return Response()