from flask import Flask, url_for, redirect

app = Flask(__name__,static_url_path= "", static_folder= "staticpages")

@app.route("/")

def index():
    return "<h1>hi there again</h1>"

@app.route("/users", methods=["GET"])
def get_users():
    return "getting all users"

@app.route("/users/<username>", methods=["GET"])
def get_user_by_name(username):
    return f"hello {username}"

@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    return f"hello your id is {id}"

@app.route("/users", methods=["POST"])
def create_user():
    return "creating users"

@app.route("/users", methods=["PUT"])
def update_user():
    return "updating users"

@app.route("/invalid", methods=["GET"])
def testing():
    return redirect(url_for("index"))


@app.route("/square/<int:num>", methods=["GET"])
def square(num):
    return f"the square of {num} is {num**2}"

if __name__ == "__main__":
    app.run(debug=True)
