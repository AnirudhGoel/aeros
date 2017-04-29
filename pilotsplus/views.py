import os
import sys
import requests
from django.shortcuts import render, HttpResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer

# The standard library modules

# The wget module
# import wget

# The BeautifulSoup module
# from bs4 import BeautifulSoup

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def index(request):
	baseurl = "https://uk.flightaware.com/live/flight/GOW544"

	driver = webdriver.Chrome("/Users/anirudhgoel/Downloads/chromedriver") # if you want to use chrome, replace Firefox() with Chrome()
	driver.get(baseurl) # load the web page

	WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CLASS_NAME, "halfButton"))) # waits till the element with the specific id appears
	src = driver.page_source # gets the html source of the page

	soup = BeautifulSoup(src) # initialize the parser and parse the source "src"
	for link in soup.find_all('a'):
		if str(link.get('href'))[0:6] == "/live/" and str(link.get('href'))[::-1][0:9] == "golkcart/":
			ext_link = link.get('href')
			break
	# list_of_attributes = {"class" : "some-class"} # A list of attributes that you want to check in a tag
	# tag = parser.findAll('video',attrs=list_of_attributes)

	base = "https://uk.flightaware.com"

	complete_url = base + ext_link

	return HttpResponse(complete_url)
	# links = []
	# for div in soup2.findAll('div'):
	# 	links.append(div.find('a')['href'])
		# print div.find('a').contents[0]
		# print div.find('img')['src']
	# print(soup.prettify())