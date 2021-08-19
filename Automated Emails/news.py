import requests
from pprint import pprint


class NewsFeed:

    """"
    Representing multiple titles and links as single string
    """
    api_key = '61e9398ee41347399634effd710c6e52'


    def __init__(self, interest, from_date, to_date, language) -> None:
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
    
    def get(self):
            
        url = self._build_url()


        articles = self._get_articles()(url)

        email_body=''
        for article in articles:
            email_body = email_body + article['title'] + "\n" +article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"https://newsapi.org/v2/everything?" \
                f"qInTitle={self.interest}&"\
                f"from={self.from_date}&" \
                f"to={self.to_date}&" \
                f"language ={self.language}&" \
                f"sortBy=popularity&" \
                f"apiKey={self.api_key}"
        return url

if __name__=='__main__':
    new_feed= NewsFeed(interest='India',from_date='2021-08-15', to_date='2021-08-18',language='en')
    print(new_feed.get())