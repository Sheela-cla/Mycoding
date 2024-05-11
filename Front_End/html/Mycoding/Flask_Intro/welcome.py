from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the page!"

@app.route('/information')
def info():
    return render_template("information.html")

@app.errorhandler(404)
def error404(e):
    return render_template("page_not_found.html"),404




if __name__=="__main__":
    app.run(debug=True)
