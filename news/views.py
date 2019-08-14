from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from newsapi import NewsApiClient
import json

#s=input("query")
#top_headlines = newsapi.get_top_headlines(sources=s,language='en')
#print(type(top_headlines))
#print(top_headlines)
#print(json.dumps(top_headlines,indent=4, separators=(". ", " = ")))

# print()

class NewsHeadlines(APIView):
    def get(self,request):
        newsapi = NewsApiClient(api_key='0fdeb4f40f0a43a9a8227e99228c1201')
        s='bbc-news,the-verge'
        if 'query' in request.GET:
            s=request.GET['query']

        all_articles = newsapi.get_everything(
                                      sources=s,
                                      
                                      
                                      language='en',
                                      sort_by='relevancy',
                                      )
        return Response(all_articles)