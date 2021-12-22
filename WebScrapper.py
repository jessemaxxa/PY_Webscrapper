import requests
from bs4 import BeautifulSoup


URL = "https://skagit.craigslist.org/d/free-stuff/search/zip"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="search-results")
print(results.prettify())

python_job_elements = results.find_all("li", class_="result-row" )

for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print( link_url)

    # print(job_element.text.strip())
#    post_links = job_element.find("a", class_="result-title hdrlnk")
#    company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#links = job_element.find_all("a")
#for link in links:
#   for link in links:
# pply here: {link_url}\n")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# # python_jobs = results.find_all("h2", string="Python") 

# # above code has to be modified because string function is case sensitve

# python_jobs = results.find_all(
#     "h2", string=lambda text: "python" in text.lower()
# )

# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs
# ]

