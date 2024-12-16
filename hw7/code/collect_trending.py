import argparse
import bs4
import requests
from fake_useragent import UserAgent
import json

GAZETTE_URL = "https://montrealgazette.com"
UA = {'User-Agent': str(UserAgent().random)}

def trending_urls():
    r = requests.get(GAZETTE_URL+"/category/news", headers=UA)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    trending = soup.find('ol', attrs={'class': 'list-widget__content list-unstyled'})
    
    links = []
    for link in trending.find_all('div', attrs={'class': 'article-card__content'}):
        links.append(link.a['href'])
    return links

def article_info(url):
    r = requests.get(GAZETTE_URL+url, headers=UA)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    header = soup.find('div', attrs={'class': 'article-header__detail__texts'})

    info ={}
    info['title'] = header.h1.text.strip()
    info['publication_date'] = header.find('span', attrs={'class': 'published-date__since'}).text.strip()

    info['author'] = header.find('span', attrs={'class': 'published-by__author'})
    if info['author'] is None :
        info['author'] = header.find('div', attrs={'class': "wire-published-by__authors"})   
    info['author'] = info['author'].text.strip()
    
    info['blurb'] = header.p.text.strip()
    return info
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', help="Output File Name", required=True)
    args = parser.parse_args()
    
    urls = trending_urls()

    info = []
    for url in urls:
        info.append(article_info(url))
    
    with open(args.output_file, 'w') as f:
        json.dump(info, f, indent=4)