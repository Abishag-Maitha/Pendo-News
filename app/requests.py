import urllib.request, json

from app import models
from .models import Source, Article


api_key="bededba7caf540958311ac6ae03f74a1"
source_url="https://newsapi.org/v2/top-headlines/sources?apiKey={}"
articles_url="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"

def get_sources():
    '''
    this is a function that fetches source information
    '''
    fetch_url=source_url.format(api_key)
    with urllib.request.urlopen(fetch_url)as url:
        data=url.read()
        jdata=json.loads(data)

        source_results=None
        if jdata["sources"]:
            source_list=jdata.sources
            source_results=process(source_list)
    return source_results

def process(source_list):
    '''
    the function creates a new list using the class source as a blueprint
    '''
    source_results=[]
    for source in source_list:
        id=source.get("id")
        name=source.get("name")
        description=source.get("description")
        url=source.get("url")
        category=source.get("category")
        language=source.get("language")
        country=source.get("country")
        if language=="en":
            source_object=Source(id,name,description,url,category,language,country)


