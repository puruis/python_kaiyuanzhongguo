import re

import requests as requests
from bs4 import BeautifulSoup

from mysqlDB import insert


def openUrl(url):
        res = requests.get(url)
        return res.text

def getTags(html,class_name):
    reg = r'<div class="'+class_name+'"></div>'
    pattern= re.compile(reg)
    tags= re.findall(pattern, html)
    return tags

def parserData(html):
    soup_string = BeautifulSoup(html, "html.parser")
    # cheilds = soup_string.find(id="newsList")
    h3_list = soup_string.findAll('h3')
    for child in h3_list:
        href_link = child.a.get('href')
        if "https://www" in href_link:
            print(href_link)
            res = openUrl(href_link)
            parserArticle(res)


def parserArticle(html):
    soup_string = BeautifulSoup(html, "html.parser")
    cheilds = soup_string.find('h2')
    article_title = cheilds.string
    author_photo = ''
    if soup_string.select('.osc-avatar')[0].img:
        author_name = soup_string.select('.osc-avatar')[0].img.get('alt')
        author_photo = soup_string.select('.osc-avatar')[0].img.get('src')
    if soup_string.select('.osc-avatar')[0].span:
        author_name = soup_string.select('.osc-avatar')[0].contents

    if soup_string.select('.extra .item'):
        release_time = soup_string.select('.extra .item')[0].contents[2]
    if soup_string.select('.list .item'):
        release_time = soup_string.select('.list .item')[0].contents[2]
    article_content = soup_string.find(id='articleContent')
    news_links = ''
    print(article_title)
    if soup_string.select('.news-links'):
        news_links = soup_string.select('.news-links')[0]

    insert(article_title,author_name,author_photo,release_time,article_content,news_links)
    # tag = getTags(mainScreen.prettify(),'item')
    # print(tag)

for index in range(1000):
    try:
        html = openUrl('https://www.oschina.net/news/widgets/_news_index_generic_list?p=%s&type=ajax' %(index))
        parserData(html)
    except:
        pass