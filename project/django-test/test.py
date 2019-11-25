import requests
def hello():
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    text = res.content.decode('utf-8')
    print(text)

if __name__ == "__main__":
    hello()