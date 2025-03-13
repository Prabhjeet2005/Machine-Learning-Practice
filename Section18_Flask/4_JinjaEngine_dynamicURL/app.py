from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/form1",methods=["GET","POST"])
def form1():
  if request.method == 'POST':
    name = request.form['formname']
    return f"Hi {name}"
  return render_template('form.html')

if __name__ == "__main__":
  app.run(debug=True)