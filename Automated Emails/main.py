import time
import yagmail
from yagmail import password
import pandas as pd
from news import NewsFeed, new_feed
import datetime

def send_email(row):
        yesterday_dt = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        today_dt =datetime.datetime.now().strftime('%Y-%m-%d')
        news_feed = NewsFeed(interest=row['interest'],
                                        from_date=yesterday_dt,
                                        to_date=today_dt,
                                        language='en')

        email = yagmail.SMTP(user='accharya.arvind@gmail.com', password='@Rvind83')

        email.send(to=row[2],
                subject=f'Your {row["interest"]} news for today',
                contents=f'Hi {row["name"]}\n, see what\'s on \
                        about {row["interest"]} today. {news_feed.get()}\nArvind',
                        attachments='people.xlsx')

while True:
        if datetime.datetime.now().hour==21 and datetime.datetime.now().minute==19:

                df = pd.read_excel('people.xlsx')
                for index, row in df.iterrows():
                        send_email(row)
        time.sleep(60)
