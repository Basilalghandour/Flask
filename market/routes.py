from market import app
from flask import render_template
from market.models import Item

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('Home.html')

@app.route("/market")



def market_page():
 
    items = Item.query.all()


    return render_template("Market.html",items=items)

