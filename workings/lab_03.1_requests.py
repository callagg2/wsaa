from urllib import response

import requests
url = "https://andrewbeatty1.pythonanywhere.com/books"
id = 1723
book = {'author': 'Joe Smith', 'id': 1677, 'price': 20, 'title': 'New Book'}
newbook = {'author': 'MaryAnn Doe', 'price': 14.99, 'title': 'Another Book'}

def readbooks():
    response = requests.get(url)
    print(response.status_code) # check for status code
    return response.json()

def createbook(book):
    response = requests.post(url,json=book)
    print(response.status_code) # check for status code
    return response.json()

def findbyid(id):
    try:
        geturl = (url + "/" + str(id))
        response = requests.get(geturl)
        print(response.status_code) # check for status code
        return response.json()
    except requests.RequestException:
        #print(f"Error occurred: Book with id {id} not found.")
        return None

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
    #print(findbyid(1701))
    #print(updatebook(id, book))
    print(deletebook(id))

