from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('Home.html')

@app.route("/market")



def market_page():
 
    items = Item.query.all()


    return render_template("Market.html",items=items)

