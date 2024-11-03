import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    print("page fetched successfully!")
else:
    print("Failed to retrieve the page.")

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_titles = []
book_prices = []

for book in books:
    title = book.h3.a["title"] 
    price = book.find("p", class_="price_color").text

    book_titles.append(title)
    book_prices.append(price)

print("Titles:", book_titles)
print("prices:", book_prices)

books_df = pd.DataFrame({
    "Title": book_titles,
    "Price": book_prices
})


print(books_df)

books_df = pd.DataFrame({
    "Title": book_titles,
    "price": book_prices
})

books_df.to_csv("books_data.csv", index=False)

print("Data saved to books_data.csv")
