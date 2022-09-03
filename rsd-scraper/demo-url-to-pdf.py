import requests
import urllib.request

import os


def download_pdf(url, file_name, headers):
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)
        

def url2pdf(url):     
    # Define HTTP Headers
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }
    # headers = { "User-Agent": "Chrome/51.0.2704.103", }
                
    # file_name='dropping.pdf'        
    drive, path_and_file = os.path.splitdrive(url)
    path, file_name = os.path.split(path_and_file)    
    print(file_name)
    
    download_pdf(url, file_name, headers)
    

url = "https://arxiv.org/pdf/2209.00626.pdf"
url2pdf(url)
