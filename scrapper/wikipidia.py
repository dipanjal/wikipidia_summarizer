import urllib.request as request
from bs4 import BeautifulSoup
import re


class wikipidia:

    def do_scrap(self, url):

        response = {
            'code': 200,
            'body': '',
            'message': 'successful'
        }

        try:
            scraped_data = request.urlopen(url).read()
            parsed_article = BeautifulSoup(scraped_data, 'html.parser')
            paragraphs = parsed_article.find_all('p')
            article_text = ""

            for passage in paragraphs:
                article_text += passage.text

            article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
            # article_text = re.sub(r'\s+', ' ', article_text)
            response['body'] = article_text.strip()

        except request.HTTPError as http_error:
            response['code'] = http_error.code
            response['message'] = http_error.msg

        return response



