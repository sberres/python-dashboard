import requests
import json
from crossref.restful import Works
works = Works()

def get_citing_articles(doi):
    articles = []
    API_CALL_CIT= "https://opencitations.net/index/coci/api/v1/citations/"
    API_CALL = API_CALL_CIT + doi
    HTTP_HEADERS = {"authorization": "YOUR-OPENCITATIONS-ACCESS-TOKEN"} # You can read the FAQs and get your token here: https://opencitations.net/accesstoken 
    HTTP_HEADERS = {"authorization": "8bd01ec8-0c5e-44fc-9b56-c7b7565dd487"}
    response = requests.get(API_CALL, headers = HTTP_HEADERS)
    response_dict = json.loads(response.text)
    # response_dict = get_citing(doi)
    for k in range(0, len(response_dict)):
        doi = response_dict[k].get('citing')
        if(doi):
            articles.append(doi)
    return articles 

def get_cited_articles(doi):
    articles = []
    API_CALL_REF = "https://opencitations.net/index/coci/api/v1/references/"
    API_CALL = API_CALL_REF + doi
    HTTP_HEADERS = {"authorization": "8bd01ec8-0c5e-44fc-9b56-c7b7565dd487"}    
    response = requests.get(API_CALL, headers = HTTP_HEADERS)
    response_dict = json.loads(response.text)
    # response_dict = get_cited(doi)
    for k in range(0, len(response_dict)):
        doi = response_dict[k].get('cited')
        if(doi):
            articles.append(doi)
            print(doi)
    return articles 




def show_data(doi):
    dct = works.doi(doi)
    url = dct.get('URL')
    cited_count = dct.get('is-referenced-by-count')
    ref_count = dct.get('reference-count')
    title = dct.get('title')
    abstract = dct.get('abstract')
    print(doi, ', ref_cout:', ref_count, '; cited_count:', cited_count)
    # print('title:', title, '\n ref_cout:', ref_count, '; cited_count:', cited_count, ';\n abstract:', abstract, '\n\n')
    



def show_data_title(doi):
    dct = works.doi(doi)
    url = dct.get('URL')
    cited_count = dct.get('is-referenced-by-count')
    ref_count = dct.get('reference-count')
    title = dct.get('title')
    abstract = dct.get('abstract')
    print(doi, ', ref_cout:', ref_count, '; cited_count:', cited_count, '; title', title)
    # print('title:', title, '\n ref_cout:', ref_count, '; cited_count:', cited_count, ';\n abstract:', abstract, '\n\n')
    


def show_articles(article_list):
    for article in articles:
        show_data(article)

def show_articles_title(article_list):
    for article in articles:
        show_data_title(article)



doi = '10.1007/s10463-019-00720-8'






doi = '10.1016/j.jclepro.2017.06.128'

doi = '10.1155/2017/5397082' # stego

articles = get_citing_articles(doi)
show_articles(articles)



doi = '10.1155/2017/5397082' # stego
show_data(doi) 
articles = get_cited_articles(doi)
show_articles(articles)



# We start with a "bucket_list" of articles, which might be a single one or just some random choice, or reference list of a given article, or a large collection of references.
def crawl_leaves(bucket_list):
    bibliography = []
    while(bucket_list):
        article = bucket_list.pop()
        show_data(article)
        if not article in bibliography:
            bibliography.append(article)
            new_list = get_citing_articles(article) # dummy or not dummy
            for art in new_list:
                if (not art in bibliography) and (not art in bucket_list):
                    bucket_list.append(art)
    return bibliography



doi = '10.1155/2017/5397082' # stego
doi = '10.1007/978-3-030-89691-1_36' # watermark

bucket_list = []; bucket_list.append(doi)
# bucket_list = get_citing_articles(doi)
bibliography = crawl_leaves(bucket_list)
print(bibliography)


doi = '10.1007/978-3-030-89691-1_36' # watermark
articles = get_cited_articles(doi)
show_articles(articles)
    
show_articles_title(articles)