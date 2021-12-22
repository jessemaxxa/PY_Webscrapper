def load_page(page):
	web_page = requests.get(page)
	soup = BeautifulSoup(web_page.content, "html.parser")
	