from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mission_to_Mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home();
    news_data = mongo.db.news_data.find_one()
    mars_data = mongo.db.mars_data.find_one()
    twitter_data = mongo.db.twitter_data.find_one()
    facts_data = mongo.db.facts_data.find_one()
    hemi_data = mongo.db.hemi_data.find_one()
    return render_template("index.html", text="Mission to Mars", news_data=news_data, mars_data=mars_data, 
    twitter_data=twitter_data, facts_data=facts_data, hemi_data=hemi_data)

@app.route("/scrape")
def scrape();
    news_data = mongo.db.news_data
    news_scrape_data = Mission_to_Mars.scrape_news()
    news_data.update({},news_scrape_data,upsert=True)

    mars_data = mongo.db.mars_data
    mars_scrape_data = Mission_to_Mars.scrape_mars()
    mars_data.update({},mars_scrape_data,upsert=True)

    twitter_data = mongo.db.twitter_data
    twitter_scrape_data = Mission_to_Mars.scrape_twitter()
    twitter_data.update({},twitter_scrape_data,upsert=True)

    facts_data = mongo.db.facts_data
    facts_scrape_data = Mission_to_Mars.scrape_facts()
    facts_data.update({},facts_scrape_data,upsert=True)

    hemi_data = mongo.db.hemi_data
    hemi_scrape_data = Mission_to_Mars.scrape_hemi()
    hemi_data.update({},hemi_scrape_data,upsert=True)

    return redirect("/",code=302)


if __name__ == "__main__":
app.run(debug=True)