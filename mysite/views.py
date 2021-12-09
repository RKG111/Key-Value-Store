from django.http.response import HttpResponse
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def get_data(request):                                                                              #Lists all the KEY VALUE pairs available
    data=Key_Value_pair.objects.all()
    serializer=Key_Value_Pair_Serializer(data, many= True)
    return Response({'status': 200, 'data': serializer.data})

@api_view(['GET'])
def get_value(request):                                                                             #Gives the VALUE of the requested KEY
    data=request.data

    value=Key_Value_pair.objects.filter(Key=data['key'])
    
    serializer=Key_Value_Pair_Serializer(value[0],many=False)
    
    return Response({'status': 200, 'payload': serializer.data})
    
@api_view(['GET'])
def set_value(request):                                                                             #Creates a new KEY-VALUE pair using the requested KEY and VALUE
    data=request.data

    new_Key_Value_Pair=Key_Value_pair.objects.create(Key=data['key'],Value=data['value'])
    new_Key_Value_Pair.save()

    return HttpResponse("New Key-Value pair added")
