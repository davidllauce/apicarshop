# Create your views here.
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from api.models import Score
from api.serializers import ScoreSerializer


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all().order_by('-score')[:10]
    serializer_class = ScoreSerializer


def scoreShow(request):
    url = "http://127.0.0.1:8000/scorelist"
    headers = {
        'X-Auth-Token': "17a3c1e85ac24df5b7e06f2e1f53ce0a",
        'Authorization': settings.API_KEY,
        'cache-control': "no-cache",
    }

    r = requests.request("GET", url, headers=headers)
    users = r.json()
    return render(request, 'index.html', {'users': users})

@csrf_exempt
@api_view(["POST"])
def score_save(request):
    """
      Retrieve, update or delete a code score.
      """
    email = request.data['email']
    try:
        score = Score.objects.get(email=email)
    except Score.DoesNotExist:
        if request.method == 'POST':
            serializer = ScoreSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        print("a")
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            if int(request.data['score']) > score.score:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
