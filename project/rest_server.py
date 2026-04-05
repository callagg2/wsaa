# author: Gerry Callaghan

from flask import Flask, request, jsonify, redirect, url_for, abort

app = Flask(__name__,static_url_path="", static_folder="staticpages")

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the REST API server!"

# put in explanation of jsonstring and how to use it in postman/curl
# getall
# curl http://127.0.0.1:5000/books
@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify({"message": "List of books"})

# put in explanation of jsonstring and how to use it in postman/curl
# find by id
# curl http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["GET"])
def find_book_by_id(book_id):
    return jsonify(f"Details for book with ID")
    #return jsonify({"message": f"Details for book with ID {book_id}"})

# put in explanation of jsonstring and how to use it in postman/curl
#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books
@app.route("/books", methods=["POST"])
def create_book():
    jsonstring = request.json
    #return jsonify({"message": "Book created", "data": jsonstring})
    return f"create {jsonstring}"

# put in explanation of jsonstring and how to use it in postman/curl
# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    jsonstring = request.json
    #return jsonify({"message": f"Book with ID {book_id} updated", "data": jsonstring})
    return f"update {id} {jsonstring}"


# put in explanation of jsonstring and how to use it in postman/curl
#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    #return jsonify({"message": f"Book with ID {book_id} deleted"})  
    return "delete"



id = 15
if __name__ == '__main__':
    #app.run(debug=True, host='<IP_ADDRESS>', port=5000)
    app.run(debug=True)