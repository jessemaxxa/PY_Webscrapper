import requests
from bs4 import BeautifulSoup

def load_page(page):
	web_page = requests.get(page)
	global soup
	soup = BeautifulSoup(web_page.content, "html.parser")

with open('webscapper.txt', 'r') as f:
	sites = f.read()
	print(sites)
url = sites
for ur in url:
	load_page(url)
	print(soup)
