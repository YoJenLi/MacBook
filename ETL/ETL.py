# -*- coding: utf-8 -*-
import requests
import sys
import download1
from bs4 import BeautifulSoup as bs
from time import time
from time import strftime
requests.packages.urllib3.disable_warnings()

rs=requests.session()

def getPageNumber(content):
    startIndex = content.find('index')
    endIndex = content.find('.html')
    pageNumber = content[startIndex+5 : endIndex]
    return pageNumber

def crawPage(url, article_list, push_rate):
    res = rs.get(url,verify=False)
    soup = bs(res.text,'html.parser')

    for r_ent in soup.select('div.r-ent'):
        try:
            atag=r_ent.select('div.title')[0].find('a')
            if(atag):
                URL = atag['href']
                title = r_ent.select('div.title')[0].text.strip()
                URL = 'https://www.ptt.cc' + URL
                rate = r_ent.select('div.nrec')[0].text

                if(rate):
                    comment_rate = rate
                    if rate == u'爆':
                        comment_rate = 100
                    if rate[0] == 'X':
                        comment_rate = -1 * int(rate[1])
                else:
                    comment_rate = 0

                if int(comment_rate) >= push_rate:
                    article_list.append((int(comment_rate), URL, title))
        except:
            print 'error:',URL


if __name__ == '__main__':
    start_page, page_term, push_rate, url = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
    ts = time()
    CrawlerTime = "ArticleDownload_" + strftime("%Y-%m-%d[%H-%M-%S]")
    if start_page < 0:
        res = rs.get(url,verify=False)
        soup = bs(res.text,'html.parser')
        ALLpageURL = soup.select('.btn.wide')[1]['href']
        ALLpage = start_page = int(getPageNumber(ALLpageURL))+1

    print "Analytical download page...."

    article_list = []
    for page in range(start_page, start_page - page_term, -1):
        page_url = url.strip().split('.html')[0] + str(page) + '.html'
        crawPage(page_url,article_list,push_rate)

    total = len(article_list)
    count = 0
    for hot_rate, url ,title in article_list:
        download1.store_art(CrawlerTime, url ,str(hot_rate),title)
        count += 1
        print "Download: " + str(100 * count/ total) + " %."

    print "DONE"
    print('Time {}s'.format(time() - ts))