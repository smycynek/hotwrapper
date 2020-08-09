from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
hotbits_endpoint = "https://www.fourmilab.ch/cgi-bin/Hotbits.api?nbytes=9&fmt=json&npass=1&lpass=8&pwtype=3&apikey=&pseudo=pseudo"


class GetHotBits(APIView):
  """ Proxy View """
  def get(self, request, format=None):
    response = requests.get(hotbits_endpoint)
    print(response.json())
    return Response(response.json()['data'])
