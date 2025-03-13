from flask import Flask,render_template,request
# request to access POST from html file

app = Flask(__name__)

@app.route("/home",methods=['GET'])
def home():
  return render_template("home.html")

@app.route("/form",methods=['GET','POST'])
def form():
  if request.method == 'POST':  # Handles POST request
    name = request.form["t"] # form.html ---> name = "t"
    return f"Hello {name}"
  return render_template("form.html")

if __name__ == "__main__":
  app.run(debug=True)