import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from hotwrapperapp.settings import HOTBITS_ENDPOINT

class GetHotBits(APIView):
    """ Proxy View """
    def get(self, request, format=None):
        response = requests.get(HOTBITS_ENDPOINT)
        print(response.json())
        return Response(response.json()['data'])
