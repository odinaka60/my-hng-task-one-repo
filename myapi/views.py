from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getEndpoints(request):

    myEndpoint = {'slackUsername': 'nagatox60', 'backend': True, 'age': 25, 'bio': 'i am odinaka from Anambra state Nigeria'}
    return Response(myEndpoint)


@api_view(['GET'])
def home(request):

    myHome = ['This is Home']
    return Response(myHome)
