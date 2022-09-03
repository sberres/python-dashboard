# scrapes a single url
# returns a list of URLs
#
import requests
from bs4 import BeautifulSoup

# Define the homepage url
# url = "http://th-ab.de"

def url2urls(url):
    link_list=[]

    # Download the homepage
    homepage = requests.get(url)
    # Create a Beautiful Soup object 
    homepage_soup = BeautifulSoup(homepage.content, features="lxml")
    # print(homepage_soup.prettify())

    # Create a list of urls linked to from the homepage
    links = homepage_soup.find_all('a')

    for link in links:
        # print just the url that the link links to
        link_list.append(link)
        
    return links
   

def rsd_filter(link_list):
    filtered_links = []
    ref=link.get('href')
    
    # filter
    if ref.count('-')>2:
        filtered_links.append(link)
        # print (link.get('href'))
    
    return filtered_links


url = "https://rsdsymposium.org/a-systemic-district-for-sustainable-tourism/"
link_list = url2urls(url)


for link in link_list:
    # print(link)
    print (link.get('href'))    
    
print('--------------------------')    
link_list = rsd_filter(link_list)

for link in link_list:
    # print(link)
    print (link.get('href'))    
    # print(link_list)



