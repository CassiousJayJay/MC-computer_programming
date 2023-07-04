import requests
from bs4 import BeautifulSoup

html = '''
<div class="books-list">
    <div class="book">
        <h2 class="title">Book 1</h2>
        <p class="author">Author 1</p>
        <span class="price">$10</span>
    </div>
    <div class="book">
        <h2 class="title">Book 2</h2>
        <p class="author">Author 2</p>
        <span class="price">$15</span>
    </div>
</div>
'''

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all book div elements
book_divs = soup.find_all('div', class_='book')

# Initialize a list to store books
books = []

# Iterate over each book div
for book_div in book_divs:
    # Extract title, author, and price
    title = book_div.find('h2', class_='title').text
    author = book_div.find('p', class_='author').text
    price = book_div.find('span', class_='price').text

    # Create a dictionary for the book
    book = {
        'title': title,
        'author': author,
        'price': price
    }

    # Add the book to the list
    books.append(book)

# Print the list of books
for book in books:
    print(book)