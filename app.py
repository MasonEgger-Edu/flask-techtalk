from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

memcache = {}


@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template("base.html", name=name, greetings=memcache)


@app.route("/greetings", methods=["POST"])
def greeting():
    memcache.update(request.json)
    return "Success"