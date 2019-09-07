from rest_framework.views  import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test Api View """

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview=[
            'Uses Http methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is manually mapped to URLS',
        ]

        return Response( {'message': 'Hello!', 'an_apiview':an_apiview} )
