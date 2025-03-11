from flask import Flask,render_template

# render_template("html_filename.html") ----> Redirects to template folder and check for index.html file

app = Flask(__name__)

@app.route("/")
def home():
  return 'this is home pg'

@app.route("/index")
def html_flask():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
  app.run(debug=True)