from flask import Flask, request,jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>hi there</h1>"

'''
@app.route("/inquery")
def inquery():
    name = request.args["name"] # note the square brackets, this is how we get query parameters not round brackets
    return name


@app.route("/inquery")
def dictionary_object():
    #name = request.args["name"] # note the square brackets, this is how we get query parameters not round brackets
    return request.args
'''

@app.route("/inbody", methods=["POST"])
def inbody():
    name = request.json["name"] # this is how we get the body of the request,
    #we use get_json() to parse the JSON data, again use square brackets not round brackets
    print(request.json) # this is how we print the body of the request, it will be a dictionary object
    age = request.json["age"]
    return f"you are {name} and you are {age} {type(age)} years old" # we use jsonify to convert the dictionary back to JSON format

@app.route("/user", methods=["GET"])  
def get_user():
    user = { "name": "John Doe", 
            "age": 30,
         }
    return jsonify(user)    

if __name__ == "__main__":
    app.run(debug=True)
