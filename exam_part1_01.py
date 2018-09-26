# Counting  Given a list of urls, print out the top 3 frequent filenames. 

from collections import Counter

urls = [     
    "http://www.google.com/a.txt",     
    "http://www.google.com.tw/a.txt",     
    "http://www.google.com/download/c.jpg",     
    "http://www.google.co.jp/a.txt",     
    "http://www.google.com/b.txt",     
    "https://facebook.com/movie/b.txt",     
    "http://yahoo.com/123/000/c.jpg",     
    "http://gliacloud.com/haha.png", 
] 
filename = []
for i in urls :
    j = i.split('/')
    filename.append(j[-1])


def counter(arr):
    for i in Counter(arr).most_common(3) :
        print(i)
    # return Counter(arr).most_common(3) # 返回出現頻率最高的3個字

counter(filename)

