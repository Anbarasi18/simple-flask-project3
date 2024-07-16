#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div><h1><center>Hello EveryOne!</center></h1><br><h1><center>Have a Great Day!!</center><h1></div>"
@app.route('/abc')
def good():
    return "<div><h1><center>Good Morning!</center></h1><br><h1><center>Have a Great Day!!</center><h1></div>"
@app.route('/cde')
def world():
    return "<div><h1><center>Good After Noon!</center></h1><br><h1><center>Have a Great Day!!</center><h1></div>"
if __name__=='__main__':
    app.run(debug=True)