from flask import Flask,render_template

app = Flask(__name__)



@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return "success"



if __name__ == '__main__':
    app.run()