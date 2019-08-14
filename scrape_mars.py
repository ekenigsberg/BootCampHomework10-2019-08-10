# import libraries
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

# define the function to initiatize the Splinter/ChromeDriver browser.
# chromedriver.exe is assumed to be in the same dir as the code
def init_browser():
    strPath = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **strPath, headless=False)

def scrape():
	### 1.1) IMPORT LIBS, INITIALIZE VARS, SCRAPE 3 "STATIC" PAGES, AND SAVE IN SOUP OBJECT LIST
	# define "static" list of URLs. These are the pages that can be scraped without browser interaction.
	lstURL = ['https://mars.nasa.gov/news', \
			  'https://twitter.com/marswxreport?lang=en', \
			  'https://space-facts.com/mars']
	# define list of Soup objects
	lstSoup = []
    # initialize browser
	brsr = init_browser()
	# iterate thru list of URLs and populate list of Soup objects
	for strURL in lstURL:
		# visit NASA's Mars News website
		brsr.visit(strURL)
		# pause 1 second
		time.sleep(1)
		# scrape page into Soup
		html = brsr.html
		lstSoup.append(bs(html, 'html.parser'))
		time.sleep(1)
	# quit browser
	brsr.quit()

	### 1.2) NASA MARS NEWS: GRAB LATEST TITLE AND PARAGRAPH TEXT
	# capture News Title:
	# 1) define vars to capture News Title and count errors
	news_title = ''
	intErr = 0
	# 2) get all divs with the class "image_and_description_container"
	soupIDC = lstSoup[0].find_all('div', class_='image_and_description_container')
	# 3) iterate thru divs for Title
	for tagOuter in soupIDC:
		while news_title == '':
			tagInner = tagOuter.find('div', class_='content_title')
			try:
				news_title = tagInner.text
			except AttributeError as e:
				intErr+=intErr
	# capture Paragraph Text:
	# 1) define var to capture Paragraph Text
	news_p = ''
	# 2) get all divs with the class "article_teaser_body"
	soupATB = lstSoup[0].find_all('div', class_='article_teaser_body')
	# 3) iterate thru divs for Paragraph Text
	for tagOuter in soupATB:
		while news_p == '':
			try:
				news_p = tagOuter.text
			except AttributeError as e:
				intErr+=intErr
	
	### 1.3) MARS WEATHER: GRAB TWEET TEXT
	# capture latest weather Tweet:
	mars_weather = lstSoup[1].find('p', class_='TweetTextSize').contents[0]

	### 1.4) MARS FACTS: GRAB FACTS TABLE
	# find the second table (index=1) and simplify it with prettify()
	htmlMarsFacts = lstSoup[2].find_all('table')[1].prettify()
#	(omitted the pandas code I had in the Jupyter Notebook--didn't need it)
#		# bring the HTML into pandas
#		lstMarsFacts = pd.read_html(htmlMarsFacts)
#		# note that read_html returns a list of DataFrames. we want the zeroth DataFrame.
#		dfMarsFacts = lstMarsFacts[0]
#		dfMarsFacts = dfMarsFacts.rename(columns={0:'Factoid',1:'Value'})

	### 1.5) JPL FEATURED SPACE IMAGE: GRAB FULL-SIZE IMAGE URL
	# define URL
	strURL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	# get URL of large image in several steps:
	# (1) visit page
	brsr = init_browser()
	brsr.visit(strURL)
	time.sleep(2)
	# (2) click "Full Image" button
	brsr.click_link_by_partial_text('FULL IMAGE')
	time.sleep(2)
	# (3) click "more info" button
	brsr.click_link_by_partial_text('more info')
	time.sleep(2)
	# (4) grab href of img tab with the "main_image" class
	html = brsr.html
	soupImg = bs(html, 'html.parser')
	brsr.quit()
	featured_image_url = 'https://www.jpl.nasa.gov' + soupImg.find('img', class_='main_image')['src']

	### 1.6) MARS HEMISPHERES: GRAB HEMISPHERES' IMAGES AND NAMES
	# define URL
	strURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	# get URLs of four hemispheres' images in several steps:
	# (1) visit page
	brsr = init_browser()
	brsr.visit(strURL)
	time.sleep(2)
	# (2) define Hemispheres list, capture links
	lstHemi = []
	html = brsr.html
	soupHemi = bs(html, 'html.parser')
	for tag in soupHemi.find_all('a', class_='itemLink product-item'):
		strURL = 'https://astrogeology.usgs.gov' + tag['href']
		if(len(lstHemi) == 0 or lstHemi[-1] != strURL):
			lstHemi.append('https://astrogeology.usgs.gov' + tag['href'])
	lstHemi
	# (3) define hemisphere_image_urls, navigate to each page and populate hemisphere_image_urls
	hemisphere_image_urls = []
	for strURL in lstHemi:
		brsr.visit(strURL)
		time.sleep(2)
		html = brsr.html
		soupHemiPg = bs(html, 'html.parser')
		hemisphere_image_urls.append( \
			{'title': soupHemiPg.find('title').text.replace(' Enhanced | USGS Astrogeology Science Center', ''), \
			 'img': 'https://astrogeology.usgs.gov' + soupHemiPg.find('img', class_='wide-image')['src']})
	brsr.quit()
	
	### 2.1) SLAM ALL SCRAPED DATA INTO ONE DICTIONARY
	dict = {'news_title':news_title, \
			'news_p':news_p,\
			'featured_image_url':featured_image_url,\
			'mars_weather':mars_weather,\
			'mars_facts':htmlMarsFacts,\
			'hemisphere_image_urls':hemisphere_image_urls}
    # return results
	return dict