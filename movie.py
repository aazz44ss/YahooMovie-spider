# -*- coding: utf-8 -*-
import urllib
from BeautifulSoup import *


id_start = raw_input('開始id: ')
number = int(raw_input('幾個: '))

for i in range(number):
    url = 'https://tw.movies.yahoo.com/movieinfo_main.html/id=' + id_start
    data = urllib.urlopen(url).read()
    soup = BeautifulSoup(data)

    try:
        movie = soup.find('div',{'class':'text bulletin'})
        img = movie.img.get('src')
        
        #中文名
        titleCh = movie.h4.string
        
        #英文名
        titleEn = movie.h5.string

        info = movie.findAll('p') #找出其他資訊的位置
        
        #上映日期
        date = info[0].contents[1].string

        #將電影類型存成list
        types = list()
        for type1 in info[1].contents[1].findAll('a'):
            types.append(type1.string)
    
        #片長
        time = info[2].contents[1].string

        #將導演存成list
        directors = list()
        for director in info[3].contents[1].findAll('a'):
            directors.append(director.string)

        #將演員存成list
        actors = list()
        for actor in info[4].contents[1].findAll('a'):
            actors.append(actor.string)
        
        #發行公司
        producer = info[5].contents[1].string

        #網站
        site = info[6].contents[1].next.string

        #劇情簡介
        movie2 = soup.find('div',{'id':'ymvs'})
        abstract = movie2.contents[3].p.getText('\n')

        import json
        import codecs
        d = {"id":id_start, "img":img, "MovieNameCh":titleCh, "MovieNameEn":titleEn, "date":date, "director":directors, "actors":actors, "producer":producer, "site":site, "abstract":abstract}
        data1 = codecs.open('movie.json','a','utf-8')
        data1.write(json.dumps(d,sort_keys=True,indent=4,ensure_ascii=False)+',')
        data1.close()

    except:
        print 'error: ' + url

    print id_start
    id_start = str(int(id_start) + 1)
