import requests
from bs4 import BeautifulSoup

class CSGOSTASH:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
        self.url = 'https://csgostash.com/weapon/'

  def key_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    return keywords

  def search(self, keywords):
    response = requests.get(self.url+keywords, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_links = soup.findAll('a')
    return result_links
      