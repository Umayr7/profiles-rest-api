from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """ Test Api View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview=[
            'Uses Http methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is manually mapped to URLS',
        ]

        return Response( {'message':'Hello!', 'an_apiview':an_apiview} )

    def post(self, request):
        """ Create a hello message with our posted name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response( {'message':message} )
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def put(self,request, pk=None):
        """ Handle updating an object """
        return Response( {'methtod':'PUT'} )

    def patch(self,request, pk=None):
        """ Handle partial update of an object """
        return Response( {'methtod':'PATCH'} )

    def delete(self,request, pk=None):
        """ Delete an object """
        return Response( {'methtod':'DELETE'} )
