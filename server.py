from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def form_posting():
    place = request.form['text']
    return place

if __name__ == '__main__':
    app.debug = True
    app.run()
