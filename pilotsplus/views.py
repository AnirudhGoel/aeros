import os
import sys
import requests
import json
from django.shortcuts import render, HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer

import sslresolved
from lxml import html

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create your views here.
	

def calc(request, f_code):
	# baseurl = "https://uk.flightaware.com/live/flight/GOW544"
	baseurl = "https://uk.flightaware.com/live/flight/" + f_code

	driver = webdriver.Chrome("/Users/anirudhgoel/Downloads/chromedriver") # if you want to use chrome, replace Firefox() with Chrome()
	driver.get(baseurl) # load the web page
	WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CLASS_NAME, "halfButton"))) # waits till the element with the specific id appears
	src = driver.page_source # gets the html source of the page

	soup = BeautifulSoup(src) # initialize the parser and parse the source "src"
	for link in soup.find_all('a'):
		if str(link.get('href'))[0:6] == "/live/" and str(link.get('href'))[::-1][0:9] == "golkcart/":
			ext_link = link.get('href')
			break
	

	base = "https://uk.flightaware.com"
	complete_url = base + ext_link

	# complete_url = "https://uk.flightaware.com/live/flight/GOW544/history/20170429/1700Z/VIDP/VABB/tracklog"

	driver = webdriver.Chrome("/Users/anirudhgoel/Downloads/chromedriver") # if you want to use chrome, replace Firefox() with Chrome()
	driver.get(complete_url) # load the web page
	WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "tracklogTable"))) # waits till the element with the specific id appears
	src = driver.page_source # gets the html source of the page

	soup2 = BeautifulSoup(src) # initialize the parser and parse the source "src"

	tr = soup2.find_all('tr', attrs= {"class" : "smallrow2"})
	td_list = tr[len(tr)-2].find_all('td')
	final_td = td_list[1:3]
	lat = final_td[0].find_all('span')
	lat = lat[0].string
	lon = final_td[1].find_all('span')
	lon = lon[0].string
	# list_of_attributes = {"class" : "some-class"} # A list of attributes that you want to check in a tag
	# tag = parser.findAll('video',attrs=list_of_attributes)

	stateFromLatLng = "http://api.geonames.org/findNearbyPlaceNameJSON?formatted=true&lat=" + lat + "&lng=" + lon + "%20&username=demo&style=full"

	data = BeautifulSoup(urlopen(stateFromLatLng))
	data = json.loads(str(data))
	state = data["geonames"][0]["adminName1"]
    

	page = requests.get('https://www.britannica.com/place/%s') % state
	tree = html.fromstring(page.content)

	data = tree.xpath('//*[@id="content"]/div[2]/div[2]/div/div/article/text()')

	data = ''.join(data)


	
	foursquare = "https://api.foursquare.com/v2/venues/explore?ll=%s,%s" % lat, lon

	info = BeautifulSoup(urlopen(foursquare))
	info = json.loads(str(info))

	name = info["venue"]["name"]

	formatted_address = info["venue"]["formattedAddress"]

	object_list = [data,name,formatted_address]

	context = {
	'object_list' : object_list
	}

	return render(request, 'data.html', {})


	



