from flask import Flask , render_template
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return "welcome to Flask" 

@app.route('/about') 
def about(): 
    return "welcome to About Page" 

@app.route('/index') 
def index(): 
    return render_template('index.html') 

@app.route('/contact') 
def contact(): 
    return "<h1>contact page</h1>"



 
if __name__ == '__main__': 
    app.run(debug=True)