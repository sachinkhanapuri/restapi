from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from qv1.models import student
from qv1.serializers import studentserializer
from django.shortcuts import render


# Create your views here.

""" function based view for GET and POST method fetching all data:
    1.GET method: used for only reading the data,we are using 
                    [obj=model_name.objects.all()
                    serializers=serializers_name(obj)
                    return Response(data=serializers.data,status=status.HTTP_201_created) ]

    2.POST method: used for both writing and reading data,we are using
                    [serializer=serializer_name(data=request.data)
                    if serializer.is_vaild():
                        serializer.save()
                        return Response(data=serializers.data,status=status.HTTP_201_created) ]             
"""
@api_view(['GET','POST'])
def student_info(request):
    if request.method=='GET':
        obj=student.objects.all()
        serializers=studentserializer(obj,many=True)
        return Response(data=serializers.data,status=status.HTTP_201_CREATED)

    elif request.method=='POST':
        serializers=studentserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.error,status=status.HTTP_400_BAD_REQUEST) 

    

"""  function base view for GET method for fetching a particular data:

     1.GET method:pk generating
                    [try:
                        obj=model_name.object.all(pk)
                    except model error_name:
                        return Response(status=status.HTTP_404_NOT_FOUND)
                        
                        if request.model=='GET':
                             serializers=serializer_name(obj)
                            return Response(data=serializers.data)
                        ]
 """            

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        obj=student.objects.get(id=pk)      
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=studentserializer(obj)
        return Response(data=serializers.data,status=status.HTTP_201_CREATED)

    elif request.method=='PUT':
        serializers=studentserializer(obj,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data,status=status.HTTP_201_CREATED)

    elif request.method=='DELETE':
        obj.delete()
        return Response()
    

    

def show_detail(request):
    data=student.objects.all()
    return render(request,"home.html",{'data1':data})