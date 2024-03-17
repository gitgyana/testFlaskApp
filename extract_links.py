import requests
from bs4 import BeautifulSoup
import re

def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        # Extracting links from 'a' tags
        for link in soup.find_all('a', href=True):
            links.append(link['href'])

        # Extracting links from 'img' tags
        for img in soup.find_all('img', src=True):
            links.append(img['src'])

        # Extracting links from 'link' tags
        for link in soup.find_all('link', href=True):
            links.append(link['href'])

        # Extracting links from 'script' tags
        for script in soup.find_all('script', src=True):
            links.append(script['src'])

        # Extracting links from 'source' tags
        for source in soup.find_all('source', src=True):
            links.append(source['src'])

        # Extracting links from inline 'style' attributes
        style_links = re.findall(r'url\((.*?)\)', response.text)
        links.extend(style_links)

        # Extracting links from 'iframe' tags
        for iframe in soup.find_all('iframe', src=True):
            links.append(iframe['src'])

        # Removing duplicate links
        links = list(set(links))
        
        return links
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_links_to_file(links, filename="links.txt"):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')
