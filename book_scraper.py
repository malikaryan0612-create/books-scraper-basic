import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

books_data = []

articles = soup.find_all('article', class_='product_pod')

for article in articles:
    title  = article.h3.a['title']
    price  = article.find('p', class_='price_color').text
    rating = article.p['class'][1]  # gives 'One', 'Two', 'Three' etc.
    
    books_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating
    })

df = pd.DataFrame(books_data)
df.to_excel("books_with_ratings.xlsx", index=False)
print(f"Done! Scraped {len(books_data)} books")