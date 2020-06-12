from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from qv1.models import student

@api_view(['GET','POST'])
def index(request):
    #print(request.user)
    #print(request.auth)
    if request.method=='GET':
        message="hello world!!!!in the world21111"
        return Response(data=message.data,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='POST':
        return Response(data=request.data, status=status.HTTP_404_NOT_FOUND)



