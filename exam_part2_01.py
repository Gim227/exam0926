# a) 請用 Python 寫出一個可以爬 ptt /reddit 任意看板（https://www.ptt.cc ）的爬蟲 程式，可以使用任意 Python 套件
import codecs   # 文字語系編碼
import requests 
import pyquery
import time
import urllib.parse as UP

def main():
    response = requests.get("https://www.ptt.cc/bbs/NBA/index6227.html")
    if response.status_code == 200 :
        # 開啟 UTF-8 編碼的文字檔  把一開始讀取的網頁存下來 write 會複寫
        f = codecs.open('nba.txt','w',encoding='utf-8')
        f.write(response.text)
        f.close()

        d = pyquery.PyQuery(response.text)
        posts = d ('div.title a')
        # print(results)
        for post in posts.items():
            # 讀取連結
            link = post('a').attr('href')
            # print(link)
            # 抓取單筆
            grabPage(link)   #標題不完全，所以回爬
            # 每次存取間隔一秒文章
            # time.sleep(0.5)   
    else:
        print("搜尋結果回傳代碼並非200")

# 抓取單筆文章
def grabPage(link):
    # 判斷連結是否有效
    link = "https://www.ptt.cc"+link
    if link is None:
        return
    # print(title)
    # print(link)
    response = requests.get(link)
    
    if response.status_code == 200:
        # 開啟 UTF-8 編碼的文字檔
        f = codecs.open('nbanews.txt', 'w', encoding='utf-8')
        f.write(response.text)
        f.close()
        
        d = pyquery.PyQuery(response.text)
        article = d('d.article-metaline span')
        print("作者 : ", article.text())
        
        
    else:
        print("搜尋結果回傳代碼並非200")

if __name__ == "__main__" :
    main()

