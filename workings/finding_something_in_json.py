
import json
with open('andrew_beattys_books.json') as f:
    data = json.load(f)

for book in data:
    if book['id'] == 1713:
        print(book['title'])
        break
else:
    print("Book with id 1713 not found.")

