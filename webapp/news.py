import requests
from datetime import datetime
from webapp.model import db, News
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

#if __name__ == "__main__":
#        html = get_html("https://www.python.org/blogs/")
#        if html:
#            with open("python-org-news.html", "w", encoding="utf8") as f:
#                f.write(html)

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find('ul', class_='list-recent-posts').findAll('li')
        news = []
        for n in news_list:
            title = n.find('a').text
            url = n.find('a')['href']
            published = n.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except(ValueError):
                published = datetime.now()
            save_news(title, url, published)
        """ news.append({
                'title' : title,
                'url' : url,
                'published' : published
            })
        return news """
    return False

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()

if __name__ == "__main__":
    html = get_html("https://www.python.org/blogs/")
    if html:
        news = get_python_news(html)
        print(news)