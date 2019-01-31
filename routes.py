from flask  import Flask, render_template,request,redirect,url_for
from app import app
from search import Searcher

searcher = Searcher()
@app.route('/', methods=['POST', 'GET'])
def video():
    if request.method == 'POST':
        SearchedLink = request.form['seachedLink']
        print("UHFDSHDFHHKFDSKJFDSNHKDFJHK")
        searcher.add_link(SearchedLink)
        return render_template('sync.html',videoLink = SearchedLink)
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
