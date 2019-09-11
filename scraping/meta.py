import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://cupofjo.com/")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
head = soup.find("head")
metas = head.findAll("meta")

# with open("metas.csv", "w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["tag","contents"])

for meta in metas:
    print("\n")
    print(meta)


