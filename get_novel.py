# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:51:27 2021

@author: asus
"""
#網站:小說狂人網
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import os
class one_chapter:
    chapter_title =''
    chapter_content =''

def get_novel_list():
    url_list=[]
    quote_page = input('小說列表網址:')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=quote_page, headers=headers)
    data =urllib.request.urlopen(req)
    soup = BeautifulSoup(data, 'html.parser')
    content = soup.find('ul', attrs={'class': 'nav chapter-list'})
    get_a = content.find_all('a')
    
    for i in get_a:
        a_str = 'https:'+ i['href']
        url_list.append(a_str)
        
    
    print('取得章節列表 ok~' + '\n')
    return url_list

def get_novel(novel_url_list):
    all_content=[]
    
    for i in range(len(novel_url_list)):
        one = one_chapter() 
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url= novel_url_list[i], headers=headers)
        data =urllib.request.urlopen(req)
        soup = BeautifulSoup(data, 'html.parser')
        content = soup.find('div', attrs={'class': 'content'})
        title = soup.find('div', attrs={'class': 'name'})
        get_title = title.text.strip()
        get_content = content.text.strip()
        one.chapter_title = get_title
        one.chapter_content = get_content
        all_content.append(one)
    
    print('取得所有章節內容 ok~' +'\n')
    return all_content

def Write(novel_content):
    name =input('小說名:')+'.txt'
    f = open(name, "a", encoding="utf-8")
    for  i in range(len(novel_content)):
        write_content = novel_content[i].chapter_title +'\n' + novel_content[i].chapter_content +'\n'
        f.write(write_content)
    
    f.close()
    print('寫檔 ok~' + '\n')
    os.system("pause")
        

if __name__ == '__main__':
    get_url_list = get_novel_list()
    get_all_content = get_novel(get_url_list)
    Write(get_all_content)
   
    
   

