import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.langchain.com/",
    "https://blog.langchain.dev/",
    "https://www.langchain.com/resources",
]

def get_content(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content,'html.parser')
  print(f"characters: {len(soup.text)} in {url}")

threads = []

for  url in urls:
  thread = threading.Thread(target=get_content,args=(url,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

print("All Web Pages Scraped")