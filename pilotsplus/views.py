import os
import sys
import requests
import json
from django.shortcuts import render, HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer

from django.shortcuts import render
from . import sslresolved

from lxml import html

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create your views here.

def index(request):
	context = {}
	return render(request, "index.html", context)

def f_info(request, f_code):
	context = {
		"f_code": f_code
	}
	return render(request, "f_info.html", context)



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

	# data = BeautifulSoup(urlopen(stateFromLatLng))
	# data = json.loads(str(data))
	data = requests.get(stateFromLatLng).json()
	state = data["geonames"][0]["adminName1"]
	britannicaUrl = 'https://www.britannica.com/place/' + state

	soup3 = BeautifulSoup(urlopen(britannicaUrl))
	data = str(soup3.find("article"))

	# page = requests.get('https://www.britannica.com/place/' + state)
	# tree = html.fromstring(page.content)
	# data = tree.xpath('//*[@id="content"]/div[2]/div[2]/div/div/article/text()')
	# data = ''.join(data)


	
	foursquare = "https://api.foursquare.com/v2/venues/explore?ll=" + lat + "," + lon + "&client_id=PMKVGM5O4DYPNJN3FU5FDKS3VFDXXYFFQWX3RYQMBD22AVNZ&client_secret=RVLTJ0B3HKTSNCF3WMA3TK1BVOHW0PGFPT0H0TRUUIJYEXIG&v=20170430"

	info = requests.get(foursquare).json()
	# info = BeautifulSoup(urlopen(foursquare))
	# info = json.loads(str(info))

	name = info["response"]["groups"][0]["items"][0]["venue"]["name"]
	formatted_address = info["response"]["groups"][0]["items"][0]["venue"]["location"]["formattedAddress"]

	object_list = [data,name,formatted_address]

	object_list = json.dumps(object_list)

	return HttpResponse(object_list, content_type = "application/json")