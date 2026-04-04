from urllib import response
import json
import requests

url = "https://andrewbeatty1.pythonanywhere.com/books"
id = 1712
book = {'author': 'Joe Smith', 'id': 1677, 'price': 20, 'title': 'New Book'}
newbook = {'author': 'MaryAnn Doe', 'price': 14.99, 'title': 'Another Book'}

def readbooks():
    response = requests.get(url)
    print(response.status_code) # check for status code
    return response.json()

def createbook(newbook):
    # add the new book
    response = requests.post(url,json=newbook)
    
    # check if the book was successfully added 
    try:
        response = requests.get(url)
        response.raise_for_status()
        new_book_list = response.json()
        for book in new_book_list:
            last_book_added = (book['title'])
        if last_book_added == newbook['title']:
            print_message =(f"{newbook['title']} by {newbook['author']}  was added successfully") 
        else:
            print_message =(f"{newbook['title']} by {newbook['author']} was not added successfully")
    except requests.exceptions.RequestException as e:
        print_message =(f"Error occurred: {e}") 
    
    return print_message
    
    
def findbyid(id):
    try:
        geturl = (url + "/" + str(id))
        response = requests.get(geturl)
        book_list = response.json()
        
        book_title = (book['title'])
        book_author = (book['author'])
        
        '''
        for book in book_list:
        
            if (book["id"]) == "1712":
                book_title = (book['title'])
                book_author = (book['author'])
                break
            else:
                print(f"Book with id {id} not found.")
        '''
        chosen_book = book_list['id']
        print(response.status_code) # check for status code
        #return response.json()
        print_message=(f"The book {book_title} by {book_author} with that id {id} is found.")
    except requests.RequestException:
        print_message=(f"Error occurred: Book with id {id} not found.")
        return None
    return print_message


def updatebook(id,book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    geturl = (url + "/" + str(id))
    response = requests.get(geturl)
    book_to_be_deleted = response.json()
    print(f"Book to be deleted: {book_to_be_deleted}")
    
    # Now we delete that book
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)

    # check if the delete was successful (gemini helped here https://gemini.google.com/share/1e0dfbb28400)
    try:
        geturl = (url + "/" + str(id))
        response = requests.get(geturl)
        response.raise_for_status()
        print_message =(f"{book_to_be_deleted} was not deleted successfully") 
    except requests.exceptions.RequestException as e:
        print_message =(f"{book_to_be_deleted} was deleted successfully") 
    
    return print_message    


if __name__ == "__main__":
    #print(readbooks())
    #print(createbook(newbook))
    print(findbyid(id))
    #print(updatebook(id, book))
    #print(deletebook(id))

