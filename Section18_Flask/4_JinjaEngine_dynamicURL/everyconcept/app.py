from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/result/<int:score>",methods=['GET','POST'])
def result(score):
  return render_template("result.html",results = score)

@app.route("/form",methods=['GET','POST'])
def form():
  if request.method == 'POST':
    maths = float(request.form['maths'])
    eng = float(request.form['eng'])
    science = float(request.form['science'])
    sst = float(request.form['sst'])

    avg_marks = (maths+eng+science+sst)/4
  
  else:
    return render_template('getdetails.html')
  
  return redirect(url_for('result',score = avg_marks))

if __name__ == "__main__":
  app.run(debug=True)