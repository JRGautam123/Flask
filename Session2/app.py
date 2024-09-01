from flask import Flask
app=Flask(__name__)

#dynamic urls
@app.route('/')
def home():
    return "<h1> Welcome to the Home Page</h2>"
@app.route('/welcome/<name>')
def welcome(name):
    return "<h1>Hey {} Welcome to the Home Page</h2>".format(name.title())


# redirection of URL




if __name__=="__main__":
    app.run(debug=True)