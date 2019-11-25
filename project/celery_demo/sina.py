
import json

import requests
import pymysql

"""爬取新浪新闻国内新闻数据"""
def get_spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    print(text)
    text = text.split('try{feedCardJsonpCallback(')[1]
    print(text)
    text = text.rsplit(');}catch(e){};',-1)[0]
    json_data = json.loads(text)
    print(json_data)
    datas = json_data['result']['data']
    conn = pymysql.connect(host='localhost', user='root', password='123456',
                           database='news', port=3306, charset='utf8')
    cursor = conn.cursor()
    sql = """insert into new(title, url, createtime) 
                            value(%s, %s, %s)"""
    for data in datas:
        title = data['title']
        url = data['url']
        print('==================')
        createtime = data['ctime']
        print(title)
        print(url)
        print(createtime)
        cursor.execute(sql, (title, url, createtime))
        conn.commit()
        print('-----------------')
    conn.close()
    return text



if __name__ == '__main__':

    for i in range(5):
        url = "https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback".format(i)
        get_spider(url)