# BootCampHomework10-2019-08-10

[Jupyter Notebook Solution](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/mission_to_mars.ipynb)<br/>
and<br/>
[Python/Flask Code](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/app.py) with supporting [Scraping Code](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/scrape_mars.py)<br/>
to<br/>
[Data Analytics Boot Camp Homework #10](https://github.com/the-Coding-Boot-Camp-at-UT/UTAMCB201904DATA3/blob/master/12-Web-Scraping-and-Document-Databases/Homework/Instructions/README.md)

# Screenshots: Mars App
## 1) Before Scraping
![Before Scraping](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/img/Screenshot01-before%20scrape.png)
## 2) During Scraping
![During Scraping](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/img/Screenshot02-during%20scrape.png)
## 3) After Scraping
![After Scraping](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/img/Screenshot03-after%20scrape.png)

# Technical Insights

* This synthesized of a lot of different technologies! Just for my own notes, here they are:
  * HTML, including associated technologies
    * Bootstrap
    * CSS
    * Jinja
  * Python, including libraries
    * Beautiful Soup
    * Flask
    * Pandas
    * Pymongo
    * Splinter (and the ChromeDriver executable)
    * Time
  * Mongo
* I jazzed up the Bootstrap page by rendering the Featured Picture as a background, and made the Hemispheres clickable links.
* I don't know why the assignment said to capture the Mars Facts table with Pandas.
  * I might *put* the data in a Pandas dataframe--I demonstrated that in my Jupyter Notebook for completeness.
  * But I spent a lot of time trying to figure how Pandas could scrape, and came up with nothing.
  * My [scraping code](https://github.com/ekenigsberg/BootCampHomework10-2019-08-10/blob/master/scrape_mars.py) doesn't use Pandas.
