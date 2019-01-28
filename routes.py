from flask  import Flask, render_template,request,redirect,url_for
from app import app

@app.route('/', methods=['POST', 'GET'])
def login():

    return render_template('sync.html')
