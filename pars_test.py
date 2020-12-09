import requests
from bs4 import BeautifulSoup


def parse():
    url = 'http://guitarland.by/catalog/katalog-gitar/akusticheskie-gitary/akusticheskie-gitary-cort.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 '
                      '(KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='product floatleft width33 vertical-separator')
    comps = []
    for item in items:
        comps.append({
            'title': item.find('div', class_='vmzag').get_text(strip=True),
            'price': item.find('span', class_='productPrice').get_text(strip=True)
        })
        for comp in comps:
            print(comp['title'], comp['price'])


parse()
