from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   f=open("index.html","r")
    ret=f.read()
    return ret

if __name__ =="__main__":
    app.run()
