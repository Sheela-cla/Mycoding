from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/register')
@app.route('/')
def regi():
    return render_template('register.html')

@app.route('/submission',methods=['POST','GET'])
def save():
   if request.method =='POST':
      N = request.form.get('Name')
      e= request.form.get('email')
      return render_template('submission.html',Name=N, email = e)




if __name__=="__main__":
    app.run(debug=True)
