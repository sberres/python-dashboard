# opens a set of urls in browser
#
# ...here handling the specific format like
#
# <iframe height="480" loading="lazy" src="https://drive.google.com/file/d/1V3ud1EyM0avXIhYuOd-gIe7oeWWbyUKw/preview" width="640">
# </iframe>
#
#
# <iframe [...] src= [...]
#

import webbrowser
import requests
from bs4 import BeautifulSoup

def opening(filename):
    # Using readlines()
    file = open(filename, 'r')
    lines = file.readlines()

    # Strips the newline character
    for line in lines:
        homepage_url = line         
    
        # Download the homepage
        homepage = requests.get(homepage_url)
        # Create a Beautiful Soup object 
        homepage_soup = BeautifulSoup(homepage.content, features="lxml")
        print(homepage_soup.prettify())
        
        # Create a list of links to pdf linked to from the homepage
        links = homepage_soup.find_all('iframe')
 
        for link in links:
            # print just the url that the link links to
            str=link.get('src')
            url=str[0:-7:1] # eliminate 'preview'
            print(url)
            # now !
            webbrowser.open(url, new=0, autoraise=True)
            
filename = 'rsd8-file-shortlist.txt'
opening(filename)