from flask import Flask , render_template
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return render_template('index.html')

@app.route('/another')
def another():
    return '<h2>Another</h2>'

@app.route('/user/<username>')
def show(username):
    return f"<h1>Hi {username}</h1>"

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()