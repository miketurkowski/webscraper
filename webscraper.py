import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

# function to get external references from the HTML page
def get_external_refs(url):
    try:
        # make an HTTP/S request to the specified URL
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # handle error
        print(f'Error: {e}')
        sys.exit(1)
    # parse the HTML response using the BeautifulSoup library
    soup = BeautifulSoup(response.text, 'html.parser')
    external_refs = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        # check if the link starts with 'http'
        if href is not None and href.startswith('http'):
            # get the domain name of the original URL
            original_domain = urlsplit(url).netloc
            # get the domain name of the href string
            href_domain = urlsplit(href).netloc
            # check if the domain of the href is different from the domain of the original URL
            if href_domain != original_domain:
                external_refs.add(href)
    return external_refs

if __name__ == '__main__':
    # check if exactly one command line aurgument is provided
    if len(sys.argv) != 2:
        print('Usage: python3 script.py [URL]')
        sys.exit(1)
    url= sys.argv[1]
    if not (url.startswith('http://www.') or url.startswith('https://www.')):
        print('Error: Invalid URL. Please provide a valid URL starting with http://www. or https://www.')
        sys.exit(1)
    # call the function to get external references
    external_refs = get_external_refs(url)
    # print the external references
    for ref in external_refs:
        print(ref)
    # print the count of unique external references
    print(f'Number of unique external references: {len(external_refs)}')
