from flask import Flask, request, url_for,render_template
from flask_pymongo import PyMongo,MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017/")
db=client["database"]
col=db["posts"]


@app.route('/',methods=['GET','POST'])
def search():
    post=col.find()
    return render_template('site.html',posts=post)


@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method =='POST':
        title=request.form['title']
        site=request.form['site']
        comment=request.form['comment']
        date=request.form['date']
        col.insert_one({'title':title,'site':site,'comment':comment,'date':date })
        return render_template('home.html',post='Successful')
    else:
        return render_template('home.html',post='Unsuccessful')

@app.route('/site',methods=['GET','POST'])
def sites():
    if request.method =='POST':
        flag=0
        post_title=request.form['title']
        result=col.find()
        for x in result:
            if x['title']==post_title:
                flag=1
                break
            else:
                flag=0
        if flag==1:
            return render_template('index.html',site=x['site'],comment=x['comment'],title=x['title'],date=x['date'])
        else:
            return render_template('index.html',site='NotFound')
    else:
        return render_template('index.html')

@app.route('/about')
def bout():
    return "About Page"



if __name__=="__main__":
    app.run(debug=True)