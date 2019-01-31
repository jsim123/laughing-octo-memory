from flask  import Flask, render_template,request,redirect,url_for
from app import app
from search import Searcher

searcher = Searcher()
@app.route('/', methods=['POST', 'GET'])
def video():
    vid = searcher.get_link()
    return render_template('sync.html',videoLink = vid)



@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form["phone"]
        if(url!=''):
            print("DFhsfddfshdfshkdsjfdjksdjfdsj"+ url)
            searcher.add_link(url)
            return redirect(url_for('video'))
    return render_template('home.html')
