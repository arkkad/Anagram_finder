from collections import defaultdict
import logging
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework.views import APIView

anagrams = defaultdict(list)

logger = logging.getLogger(__name__)


class AnagramDict(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.method == 'POST':
            keys = request.data
            anagram_items = list(keys)[0]
            items = anagram_items.replace('[', '').replace(']', '').replace('"', '').replace(' ', '').split(',')
            try:
                anagram_finder(items)
                logger.info('Dict of anagrams created ' + str(anagrams))
                return HttpResponse("Dictionary successfully created ", status=200)
            except Exception as ex:
                logger.error(ex)
                return HttpResponse(ex, status=400)

    def get(self, request):
        if request.method == 'GET':
            anagrams.clear()
        return HttpResponse('Dictionary successfully cleaned ', status=200)


class AnagramShowView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.method == 'GET':
            word = request.GET.get('word')
            response = anagram_showing(word)
            if response is None:
                return HttpResponse('null', status=200)
            return HttpResponse(str(response), status=200)


def anagram_finder(list_anagrams):
    for item in list_anagrams:
        key = ''.join(sorted(item.lower()))
        anagrams[key].append(item)


def anagram_showing(word):
    for key, anagram in anagrams.items():
        if key == ''.join(sorted(word.lower())):
            return anagram
