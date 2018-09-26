# b) 請用 python 寫出一個簡單的網頁，只需要一個頁面 每次瀏覽時隨機出現 the zen of python 其中一
import codecs   # 文字語系編碼
import requests 
import pyquery

def main():
    response = requests.get("http://wiki.python.org.tw/The%20Zen%20Of%20Python")
    if response.status_code == 200 :
        # 開啟 UTF-8 編碼的文字檔  把一開始讀取的網頁存下來 write 會複寫
        f = codecs.open('test.txt','w',encoding='utf-8')
        f.write(response.text)
        f.close()

        # items() 可用來把 PyQuery 取回的搜尋結果輸出成 list，方便我們 for...in 取出
        d = pyquery.PyQuery(response.text)
        results = d ('p.line874')
        for item in results.items():
            if item.text() == '':     
                continue
            # print(item.text())
            f = codecs.open('the_zen.txt','w',encoding='utf-8')
            f.write(item.text())
            f.close()    
    else:
        print("搜尋結果回傳代碼並非200")

if __name__ == "__main__" :
    main()

