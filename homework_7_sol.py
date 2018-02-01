"""
http://www.hani.co.kr/arti/opinion/column/830031.html?_fr=mt0
뉴스 내용 가져오기
"""
import urllib.request
import re
url = "http://www.hani.co.kr/arti/opinion/column/830031.html?_fr=mt0"

news_html = urllib.request.urlopen(url).read().decode("utf-8")

NEWS_PATTERN = '''<div class="article-text">.*?<div class="desc".*?</div>.*?</div>.*?</div>(.*?)</div>'''

news_pattern = re.compile(NEWS_PATTERN, re.DOTALL)
news = news_pattern.findall(news_html)[0]
news = news.replace("<P align=justify></P>", "")
print(news)


