import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/index.html" 

response = requests.get(url) 

print(response.status_code) 

#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

cards = soup.select(".product_pod")
print(cards [0]) 
all_scrapped_books = []
for card in cards:
    title = card.select_one("h3 a").text
    print( title)
    price = card.select_one(".price_color").text
    print( price)
     
    book_item = {
        "title": title,
        "price": price.replace("£", ""),
     }
    all_scrapped_books.append(book_item)

# print(all_scrapped_books)    

df = pd.DataFrame(all_scrapped_books)
#df.to_csv("scrapped_books.csv")
df.to_excel("scrapped_books.xlsx")

    
