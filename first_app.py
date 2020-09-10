from flask import Flask, request, url_for,render_template
from flask_pymongo import PyMongo,MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017/")
db=client["database"]
col=db["posts"]


@app.route('/',methods=['GET','POST'])
def search():
    if request.method =='POST':
        flag=0
        post_title=request.form['title']
        result=col.find()
        for x in result:
            if x['site']==post_title:
                flag=1
            else:
                flag=0
        if flag==1:
            return render_template('/index.html',site=x['site'],comment=x['comment'])
        else:
            return render_template('/index.html',site='NotFound',comment='NotFound')

    else:
        return render_template('index.html',site='NOTFOUND',comment='NOTFOUND')
@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method =='POST':
        site=request.form['title']
        comment=request.form['comment']
        col.insert_one({'site':site,'comment':comment})
        return 'done'
    else:
        return render_template('home.html')

@app.route('/site')
def sites():
    post=col.find()
    return render_template('site.html',posts=post)



if __name__=="__main__":
    app.run(debug=True)