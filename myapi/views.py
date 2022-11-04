from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['GET'])
def getEndpoints(request):

    myEndpoint = {'slackUsername': 'nagatox60', 'backend': True, 'age': 25, 'bio': 'i am odinaka from Anambra state Nigeria'}
    return Response(myEndpoint)


@api_view(['GET'])
def home(request):

    myHome = ['This is Home']
    return Response(myHome)

@api_view(['POST'])
@parser_classes([JSONParser])
def getResult(request, format=None):
    if request.data:
        data = request.data
        if data['operation_type'].lower() == 'addition':
            result = data['x']+data['y']
            res = {'slackUsername': 'nagatox60', 'result': result, 'operation_type': data['operation_type']}
            return Response(res)
        elif data['operation_type'].lower() == 'subtraction':
            result = data['x']-data['y']
            res = {'slackUsername': 'nagatox60', 'result': result, 'operation_type': data['operation_type']}
            return Response(res)
        elif data['operation_type'].lower() == 'multiplication':
            result = data['x']*data['y']
            res = {'slackUsername': 'nagatox60', 'result': result, 'operation_type': data['operation_type']}
            return Response(res)
        else:
            sentence = data['operation_type']
            words = sentence.split(' ')
            words = [word.lower() for word in words]
            addwords = ['add', 'addition', 'sum' ]
            substractionwords = ['subtraction', 'difference', 'subtract']
            multiplicationwords = ['multiply', 'product', 'multiplication']
            
            if bool(set(addwords) & set(words)):
                result = data['x']+data['y']
                res = {'slackUsername': 'nagatox60', 'result': result, 'operation_type': 'addition'}
                return Response(res)
            elif bool(set(substractionwords) & set(words)):
                result = data['x']-data['y']
                res = {'slackUsername': 'nagatox60', 'result': result, 'operation_type': 'subtraction'}
                return Response(res)
            elif bool(set(multiplicationwords) & set(words)):
                result = data['x']*data['y']
                res = {'slackUsername': 'nagatox60', 'result': result, 'operation_type': 'multiplication'}
                return Response(res)
            else:
                return Response('No operation type')    
    else:
        return Response('No request body')
        
    
