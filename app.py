# import libraries
from flask import Flask, render_template
import pymongo
import scrape_mars

# instantiate Flask app
app=Flask(__name__)

# establish mongo connection
conn = 'mongodb://localhost:27017'
cli = pymongo.MongoClient(conn)

# connect to mongo mars db
db = cli.planet

### 2.2) CREATE /SCRAPE PATH
@app.route('/scrape')
def mars_scrape():
	print('Server received request for "scrape" page...')
	# clear out mars collection
	db.mars.delete_many({})
	# store result of "scrape()" function in mongo
	dict = scrape_mars.scrape()
	db.mars.insert_one(dict)
	return render_template('scraping_complete.html')

### 2.3) CREATE / (ROOT) PATH
@app.route('/')
def root():
    print('Server received request for root page...')
    # pull everything from "mars" collection in "planet" database into "lstMars"
    lstMars = db.mars.find()
    # render index.html template and pass it "lstMars"
    return render_template('index.html', lst=lstMars)

if __name__ == "__main__":
    app.run(debug=True)