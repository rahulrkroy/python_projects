from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
# note that html files should be placed under templates folder only
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/bio')
def bio():
    return "I am a cse student"

if __name__=='__main__':
    app.run(debug=True)
