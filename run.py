#import scrapy
# from scrapy_pro_init.spiders.hshfy_sh_cn import *
# from scrapy_pro_init.spiders.news_china import *
# from scrapy.crawler import CrawlerProcess
#
# process = CrawlerProcess
# process.crawl(HshfyShCnSpider)
# process.crawl(NewsChinaSpider)
# process.start()

# -*-- coding:utf-8 -*--

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(5)

while True:
    try:
        connect, address = sock.accept()
        print connect, address
        buf = connect.recv(1024)
        connect.send('HTTP/1.1 200 OK\r\n\r\n')
        connect.send('Hello world')
        connect.close()

    except (Exception, KeyboardInterrupt), e:
        print e
        connect.close()
        sock.close()
        break


import logging
import json
import MySQLdb
from MySQLdb.cursors import DictCursor

conn = MySQLdb.connect('127.0.0.1', 'root', '123123', 'lawyer', cursorclass = DictCursor)
cursor = conn.cursor()

sql = "SELECT * FROM links LIMIT 10";
nn = cursor.execute(sql)
result = cursor.fetchall()
print result
cursor.close()
conn.commit()
conn.close()


a = {
    "b": {
        "c": "cccccc"
    }
}
a = ['aa', 'ccc', 'ddd', 'ccc']
print a
b = json.dumps(a)
a = json.loads(b)
print a
print a[0]

import hashlib

md5 = hashlib.md5()
md5.update('a')
print md5.hexdigest()

md5 = hashlib.md5()
md5.update('a')
print md5.hexdigest()

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

logging.debug('hello world')

if a is None:
    print 'b'
else:
    print 'c'


