from django.shortcuts import render
import sslresolved
from lxml import html
import requests

# Create your views here.
def scrape_data(request):
	query = request.GET.get('q', None)
	age = requests.get('https://www.britannica.com/place/Argentina')
	tree = html.fromstring(page.content)

	intro = tree.xpath('//*[@id="toc33101"]/p/text()')

	data = ''.join(intro)

	html = "<html><body>%s </body></html>" % data
	return HttpResponse(html)