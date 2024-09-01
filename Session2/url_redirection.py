# redirection of URL
# "its a process in which users visit a particular URL, they're navigated/directed to different URL"

from flask import Flask,redirect, url_for
import time
app=Flask(__name__)

#dynamic urls
@app.route('/')
def home():
    return "<h1> Welcome to the Home Page</h2>"

@app.route('/fail/<sname>/<int:marks>')
def fail(sname,marks):
    return "<h1> Sorry {} You've failed!!! and your marks is {}</h1>".format(sname,marks)

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
        return "<h1> Congratulations {} You've passed!!! and your score is {}</h1>".format(sname,marks)



@app.route('/score/<name>/<int:score>')
def score(name,score):
   
    if score<=30:
        time.sleep(1)
        # redirect user to the pass page
        return redirect(url_for("fail",sname=name,marks=score))
    else:
        time.sleep(1)
        # redirect user to the pass page
        return redirect(url_for('passed',sname=name,marks=score))







if __name__=="__main__":
    app.run(debug=True)