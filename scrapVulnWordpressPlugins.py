#!/usr/bin/python3 

import requests, sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
	print('\n Use: python3 ' + sys.argv[0] + ' outputFile ')
	sys.exit(1)

headers = {
	'Host': 'plugins.svn.wordpress.org',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Sec-GPC': '1',
	'If-Modified-Since': 'Wed, 10 Feb 2021 08:30:35 GMT',
	'If-None-Match': 'W/"2472212//"',
}

requestContent = requests.get('https://plugins.svn.wordpress.org/', headers=headers)
soup = BeautifulSoup(requestContent.text, 'lxml')

total = []
export = ""

for link in soup.find_all('a', href=True):
	total.append(link['href'])

for plugin in total:
	export += '%s \n' % plugin

file = open(sys.argv[1],'w+')
file.write(export);
file.close

print("S4yonara");