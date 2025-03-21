from bs4 import BeautifulSoup
import requests

def TechCrunch():
    url = "https://techcrunch.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    articles = soup.find_all("a", class_="loop-card__title-link")
    news = []
    for item in articles[:5]:  # Limit to first 5 articles
        title = item.text.strip()
        link = item["href"]
        news.append({"title": title, "link": link})
    print("Top tech news from Tech CRunch")
    for news in news:
        print(news)

def TOI():
    url="https://timesofindia.indiatimes.com/gadgets-news"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    latest_news=soup.find('ul',class_="list5 clearfix")
    articles=latest_news.find_all('span',class_="w_tle")
    news=[]
    for article in articles[:5]:
        item=article.find('a')
        link=item.get('href')
        if link.startswith("https") is False:
            link="https://timesofindia.indiatimes.com/"+link
        title=item.get('title')
        news.append({"title": title, "link": link})
    print("Top tech news from Times Of India")
    for news in news:
        print(news)
def GGL():
    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    articles=soup.find_all('article')
    news=[]
    for item in articles[:5]:
        link=item.find('a').get('href')
        link="https://news.google.com"+link[1:]
        title=item.find('button').get('aria-label')[6:]
        news.append({"title": title, "link": link})
    print("Top tech news from GOOGLE NEWS")
    for news in news:
        print(news)
TechCrunch()
TOI()
GGL()


