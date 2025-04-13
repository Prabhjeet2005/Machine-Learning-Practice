from flask import Flask

"""
instance of Flask class, it is WSGI (Web Server Gateway Interface) application

"""
app = Flask(__name__)  # __name__ is entry point


@app.route("/")
def home():
    return "This is home Route."


@app.route("/second_page")
def second_page():
    return "This is Second Page. Okay"


if __name__ == "__main__":  # Execution Starts here
    app.run(debug=True)  # debug = True -----> Automatic Restart the server
