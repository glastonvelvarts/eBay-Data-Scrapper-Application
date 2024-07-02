import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_ebay(search_query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    titles = []
    prices = []
    ratings = []  # eBay listings typically don't show ratings on the search page
    descriptions = []

    for item in soup.select('.s-item'):
        title = item.select_one('.s-item__title')
        price = item.select_one('.s-item__price')
        description = item.select_one('.s-item__subtitle')

        if title:
            titles.append(title.text)
        else:
            titles.append(None)
        
        if price:
            prices.append(price.text.replace('$', '').replace(',', '').strip())
        else:
            prices.append(None)
        
        if description:
            descriptions.append(description.text)
        else:
            descriptions.append(None)

    data = {
        'Title': titles,
        'Price': prices,
        'Description': descriptions
    }

    df = pd.DataFrame(data)
    df.to_excel('ebay_products.xlsx', index=False)
    print("Data saved to ebay_products.xlsx")

if __name__ == '__main__':
    scrape_ebay('logitech')
