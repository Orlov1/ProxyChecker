import requests
from random import choice
from progress.bar import Bar

url = 'http://yandex.ru/'
 
open("goods_proxy.txt", "w").close()

lines = sum(1 for line in open('proxy.txt', 'r'))

proxys = open('proxy.txt').read().split('\n')
useragents = open('ua.txt').read().split('\n')
bar = Bar('Выполнение ', max=lines)

for i in proxys:
    proxy = {'http':'http://' + choice(proxys)}
    HEADERS = {'User-Agent' : choice(useragents)}
    bar.next()

    try:
        req = requests.get(url, proxies=proxy, headers = HEADERS, timeout = 10)
        if req.status_code == 200:
            # print(proxy)
            # print(req.status_code)

            outfile=open('goods_proxy.txt', 'a')
            outfile.write(str(proxy) + '\n')
            outfile.close()  
        
    except:
        # print('Ошибка!')
        outfile.close()
bar.finish()                    