from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/submit',methods=['GET','POST'])
def submit():
  if request.method == 'POST':
    name = request.form['formname']
    return f"Hiii {name}"
  return render_template('form.html')

# Variable Rule ==> INPUT URL
@app.route('/success/<score>',methods=['GET','POST'])
def success(score):
    return f"Your Score From URL is {score}"  ## By Default score is string

@app.route("/exam_forloop/<score>")
def exam(score):
    res = ''
    if int(score) > 50:
      res = "PASSED"
    else:
      res = "FAILED"
    
    exp = {'score':score,'res':res}
    return render_template('examresult.html',results = exp)

@app.route("/exam_if/<int:score>")
def exam_if(score):
   return render_template('exam_if.html',results = score)
  

if __name__ == "__main__":
  app.run(debug = True)