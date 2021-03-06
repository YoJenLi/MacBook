# -*- coding: utf-8 -*-
import requests
import os
import sys
import re
from bs4 import BeautifulSoup as bs
from time import time
from functools import partial
from time import strftime
requests.packages.urllib3.disable_warnings()

rs = requests.session()

def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value.rstrip();

def store_art(CrawlerTime, url, rate="", title="" ):
    res=rs.get(url,verify=False)
    soup=bs(res.text,'html.parser')
    board = url.strip('https://www.ptt.cc/bbs/').split('/index.html')[0]
    relative_path = os.path.join(CrawlerTime,board)
    path = os.path.abspath(relative_path)
    try:
    	if not os.path.exists(path):
    		os.makedirs(path) 
    except Exception, e:
    	print 'os.makedirs(path) error' 

    filename = remove(title, '\/:*?"<>|.') + ".txt"          
    with open(CrawlerTime +"/"+ filename, 'w') as f: 
                 f.write(res.text.encode('utf-8')) 



def main():
    print "Crawler Parsing...."
    CrawlerTime= "ArticleDownload_"+strftime("%Y-%m-%d[%H-%M-%S]")
    ts = time()
    article_urls = []
    total=0
    # with open(sys.argv[1]) as fd:
    #     for url in fd:
    #         article_urls.append(url.strip())
    #         total+=1

    # count=0
    for article_url in article_urls:
        count+=1
        print "Crawling: " + str(100 * count / total ) + " %."
        store_art(CrawlerTime,board)
        
    print('Time {}s'.format(time() - ts))
    print "Crawler End...."

if __name__ == '__main__':
    main()