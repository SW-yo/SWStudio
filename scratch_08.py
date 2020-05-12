from collections import Counter
import math, random, csv, json, re

from bs4 import BeautifulSoup
import requests
import json
from dateutil.parser import parse
from twython import Twython, TwythonStreamer
from time import sleep

url = "https://www.oreilly.co.jp/catalog/soon.html"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
#soup = BeautifulSoup(requests.get(url).text, 'lxml')


tds = soup('td', 'thumbtext')
#print(len(tds))

def is_video(td):
    #pricelabelを1つだけ持ち、空白を取り除いた文字列が'Video'であれば
    #ビデオである
    pricelabels = td('spam', 'pricelabel')
    return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswitch("Video"))

#print(len([td for td in tds if not is_video(td)]))

def book_info(td):
    #与えられた<td>タグを、1冊の書籍情報を表現している。
    #ここから書籍の詳細を抜き出して、辞書として返す

    title = td.find("div", "thumbheader").a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()

    return {
        "title" : title,
        "authors" : authors,
        "isbn" : isbn,
        "date" : date
    }


endpoint = "https://api.github.com/users/joelgrus/repos"

repos = json.loads(requests.get(endpoint).text)

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repositories = sorted(repos, key=lambda r: r["created_at"], reverse=True)[:5]
last_5_languages = [repo["language"] for repo in last_5_repositories]

#print(last_5_languages)


twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)
#'data science'を含むツィートを検索する
for status in twitter.search(q='"data science"')["statuses"]:
        user = status["user"]["screen_name"].encode('utf-8')
        text = status["text"].encode('utf-8')
        print(user, ":", text)
        print()


#データを大域変数に格納するのは稚拙な方法であるが
#サンプルコードを単純にできる

tweets = []

class MyStreamer(TwythonStreamer):
    #stremとのやり取りを行う方法を定義するTwythonStreamerのサブクラス

    def on_success(self, data):
        #twitterがデータを送ってきたらどうするか？
        #ここでdataはツーとを表す

        #英語のツィートのみを対象とする
        if data['lang'] == 'en':
            tweets.append(data)
            print ("received tweet #", len(tweets))

        #十分なツィートを得られたら終了
            if len('tweets') >= 100:
                self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

print(stream)

stream.statuses.filter(track='data')

"""
top_hashtags = Counter(hashtag['text'].lower()
                for tweet in tweets
                for hashtag in tweet["entities"]["hashtags"])

print(top_hashtags.most_common(5))
"""
