from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")


if __name__ == '__main__':
    app.debug = True
    app.run()
