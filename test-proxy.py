import requests
from random import choice
from random import choice 
 
HEADERS = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17'
          }
 
url = 'http://yandex.ru/'
 
proxys = open('proxy.txt').read().split('\n')
 
for i in proxys:
    proxy = {'http':'http://' + choice(proxys)}
    
    try:
        req = requests.get(url, proxies=proxy, headers = HEADERS, timeout = 10)
        if req.status_code == 200:
            # print(proxy)
            # print(req.status_code)

            outfile=open('goods_proxy.txt', 'a')
            outfile.write(str(proxy) + '\n')
            outfile.close()  
        
    except:
        print('Ошибка!')            