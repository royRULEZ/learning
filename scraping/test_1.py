import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.busybudgeter.com/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find("div", class_="home-bottom")
sections = articles.findAll("section")

for section in sections:
    div_ = section.find("div", class_="box")
    if div_ != None:
        title_ = div_.find("h4").get_text()
        print(title_)

    #title = title_.get_text()
    #print(title)
