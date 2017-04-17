import sys
from vitsh.constants import *
import requests
from bs4 import BeautifulSoup

def cricket(args):

	sys.stdout.write('Loading live scores ... \n \n');

	default_link='http://static.cricinfo.com/rss/livescores.xml'

	try:
		r = requests.get(default_link)
		soup=BeautifulSoup(r.text,'html.parser')
		search=soup.find_all('item')


		if search:
			xml = soup.find_all("item")
			matches = map( lambda item : item.title.text, xml)
			for i in matches:
				sys.stdout.write(i+'\n')
	except requests.exceptions.RequestException as e:
		sys.stdout.write('Check network connection and Try Again !!!');

	sys.stdout.write('\n \n');

	sys.stdout.flush()

	return SHELL_STATUS_RUN