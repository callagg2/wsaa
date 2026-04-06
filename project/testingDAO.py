# testing the DAO class for database operations

from DAOfordatabase import bookDAO

book = {
    "title": "The Great Gatsby", 
    "author": "F. Scott Fitzgerald", 
    "price": 11
    }

# create a book
latest_id = bookDAO.create_book(book)
bookid = book.get("id")

# find by id
book = bookDAO.get_by_id(bookid)
print("test create and find by id")
print(book) # need to convert into dictionar y object

# read all books
print("test read all")
books = bookDAO.get_all()
for book in books:
    print(book)

# update a book
new_book = { "title": "Great Expectations",
             "author": "Charles Dickens",
             "price": 15
             }       
bookDAO.update_book(bookid, new_book)
result = bookDAO.get_by_id(bookid)
print("test update")
print(result)

# delete a book
bookDAO.delete_book(bookid) 


