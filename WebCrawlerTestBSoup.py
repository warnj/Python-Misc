import mechanize
import urllib
import json
from bs4 import BeautifulSoup

def getTimes(query,num):
    url = "http://query.nytimes.com/svc/cse/v2/sitesearch.json?query="+query.replace(" ","%20")+"&pt=article&page="+str(num)
    jtext = urllib.urlopen(url)
    return jtext




def search(term):
    page_number = 0
    meta = 1
    while meta > 0 and page_number<1:
        resp = json.load(getTimes(term,page_number))
        meta = int(resp['results']['meta']['payload'])
        for res in resp['results']['results']:
            print res['snippet']
            #headline = res['hdl']
            #snippet = res['snippet']
            #author = res['cre']
            #url1 = res['url']
            #print headline
            #print url
        page_number+=1




search("exotic cars")