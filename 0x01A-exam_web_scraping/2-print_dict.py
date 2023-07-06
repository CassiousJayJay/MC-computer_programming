from bs4 import BeautifulSoup
import requests

html =  '''
<table class="grades">
    <tr>
        <th>Student</th>
        <th>Grade</th>
     </tr>
     <tr>
        <td>John</td>
        <td>A</td>
     </tr>
     <tr>
        <td>Jane</td>
        <td>B</td>
    </tr>
</table>
'''
# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all book div elements
student_tr = soup.find_all('tr', class_='grades')

# Initialize a list to store books
books = []

# Iterate over each book div
for student_tr in students_tr:
    # Extract title, author, and price
    title = name_tr.find('th', class_='grade').text
    author = name_tr.find('td', class_='grade').text
    price = name_tr.find('td', class_='grade').text

    # Create a dictionary for the book
    details = {
        'name': name,
        'grade': grade,
        'price': price
    }

    # Add the book to the list
    books.append(book)

# Print the list of books
for book in books:
    print(book)