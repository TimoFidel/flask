from flask import Flask, render_template
from pymongo import MongoClient
from datetime import datetime

app=Flask(__name__)
client=MongoClient("mongodb://localhost:27017/")
db=client["mydatabase"]
col=db["posts"]

site=[
    {"web_link":"https://www.w3schools.com","comment":" THE WORLD'S LARGEST WEB DEVELOPER SITE","added_by":"asif","added_at":datetime.now()},
    {"web_link":"http://www.amazon.in","comment":" Online Shopping India - Buy mobiles, laptops, cameras, books, watches, apparel, shoes and e-Gift Cards. Free Shipping & Cash on Delivery ...","added_by":"asif","added_at":datetime.now()},
    {"web_link":"http://www.twitter.com","comment":"Twitter to find the latest news and world events faster. Find popular people, hashtags and photos for any topic you can imagine.","added_by":"asif","added_at":datetime.now()}
]


col.insert_many(site)

sites=col.find().limit(3)


@app.route('/')
def post():
    return render_template('index.html',posts=sites)

if __name__=="__main__":
    app.run(debug=True)