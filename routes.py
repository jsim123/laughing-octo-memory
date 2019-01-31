from flask  import Flask, render_template,request,redirect,url_for
from app import app

@app.route('/', methods=['POST', 'GET'])
def video():

    return render_template('sync.html')



@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form["phone"]
        print("DFhsfddfshdfshkdsjfdjksdjfdsj"+ url)
        return redirect(url_for('video'))
    return render_template('home.html')
