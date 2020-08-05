from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import requests
import json
hb =  "https://www.fourmilab.ch/cgi-bin/Hotbits.api?nbytes=9&fmt=json&npass=1&lpass=8&pwtype=3&apikey=&pseudo=pseudo"


class GetHotBits(APIView):
  def get(self, request, format=None):
    response = requests.get(hb)
    print(response.json())
    return Response(response.json()['data'])
