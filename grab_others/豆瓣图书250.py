import requests
from bs4 import BeautifulSoup

base_url = 'https://book.douban.com/top250?start='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
urllist = []
# 从0到225，间隔25的数组
for page in range(0, 250, 25):
    allurl = base_url + str(page)
    urllist.append(allurl)


f = open("hhhh.txt", 'w', encoding='utf-8')

for url in urllist:
    soup = BeautifulSoup(resp.text, 'html.parser')
    book_names = soup.select(".pl2 a")    
    book_authors = soup.select("p.pl")    
    book_scores = soup.select(".star .rating_nums")
    book_quotes = soup.select(".quote")    
    for book_name,book_author,book_score,book_quote in zip(book_names,book_authors,book_scores,book_quotes):
        book_name = '书名：' + str(book_name['title']) + '\n'
        book_author = '作者：' + str(book_author.get_text().split("/")[0]) + '\n'
        book_score = '评分：' + str(book_score.get_text()) + '\n'
        book_quote = '一句话：' + str(book_quote.get_text()) + '\n'
        data = book_name + book_author +book_score +book_quote
            # 保存数据
        f.writelines(data + '=======================' + '\n')
     
f.close()

#使用css解析器得到数据
#book_names = soup.select(".pl2 a")
#for book_name in book_names:
##    book_name = book_name.get_text()
#    book_name = book_name['title']
#    print(book_name)

#book_original_names = soup.select(".pl2 span")
#for book_original_name in book_original_names:
#    book_original_name = book_original_name.get_text()
##    book_original_name = book_original_name['title']
#    print(book_original_name)
    
#book_authers = soup.select("p.pl")
#for book_auther in book_authers:
#    book_auther = book_auther.get_text().split("/")[0]
#    print(book_auther)

#book_scores = soup.select(".star .rating_nums")
#for book_score in book_scores:
#    book_score = book_score.get_text()
#    print(book_score)

#book_quotes = soup.select(".quote")
#for book_quote in book_quotes:
#    book_quote = book_quote.get_text()
#    print(book_quote)
#if __name__=__main__:
#    urls = getUrls()