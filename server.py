from flask import Flask, jsonify, request, redirect, current_app, json, abort
import urllib, os, uuid
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect("0.0.0.0/index.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True)
