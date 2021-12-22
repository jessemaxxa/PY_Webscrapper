import requests
from bs4 import BeautifulSoup


URL = "https://skagit.craigslist.org/d/free-stuff/search/zip"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="search-results")
# print(results.prettify())

python_job_elements = results.find_all("li", class_="result-row" )
new_links = []
for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        
        print(link["href"])
      
print(link_url)   
    
# print(link_url)





    # for ll in link_url:
    #     if ll != #:
    #         new_links.append(ll)

            # print(new_links)

           


            # if ll == # print(link_url):
            #     link_url.remove(ll)
            
        # print(link_url)

        # if l == "#":
        #         link_url.remove(l)

        
        # page = requests.get(link_url)
        # result = soup.find("section", class_="body")
        # soup = BeautifulSoup(page.content, "html.parser")
        #print( link_url.text.strip())

