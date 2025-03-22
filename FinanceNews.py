from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def Economic_Times():
    url="https://economictimes.indiatimes.com/?from=mdr"
    page=requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    articles = soup.find_all("a", class_="tle_wrp")
    news=[]
    for article in articles[:10]:
        title = article.find("span", class_="str_title").text.strip()
        link = article["href"]
        news+=[{"title":title,"link":link}]
    print("News from Economic times:")
    for news_article in news:
        print(news_article)

def Yahoo_finance_news():
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news/"
    headers = {
            "X-RapidAPI-Key": "c78b91b3bamshd1ed19c76c62978p176704jsn676c3dff1ace",
            "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
        }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            data = response.json()  
            news_list = data.get("body", [])   

            if news_list:
                news_extracted=[]
                for news in news_list[:5]: 
                    title = news.get("title", "No Title")
                    link = news.get("link", "No Link")
                    news_extracted+=[{"title":title,"link":link}]
                print("News from Yahoo Finance:")
                for news_article in news_extracted:
                    print(news_article)
            else:
                print("No news items found in response")

    else:
            print(f"Error: {response.status_code} - {response.text}")

def GGL():
    url="https://news.google.com/search?aq=f&pz=1&cf=all&hl=en-IN&q=Finance;&gl=IN&ceid=IN:en"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    articles=soup.find_all('article')
    news=[]
    for item in articles[:5]:
        link=item.find('a').get('href')
        link="https://news.google.com"+link[1:]
        title=item.find('button').get('aria-label')[6:]
        news.append({"title": title, "link": link})
    print("Top Finance news from GOOGLE NEWS")
    for news_article in news:
        print(news_article)

def main():
    configure()
    Economic_Times()
    Yahoo_finance_news()
    GGL()
main()
