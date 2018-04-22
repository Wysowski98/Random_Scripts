#!/usr/bin/env python3
import sys

"""
Put the script in /usr/bin and do `chmod +x dict` so you can execute it in terminal using `dict word`
"""

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def main(arg = sys.argv[1]):
	page = "https://www.merriam-webster.com/dictionary/{}".format(arg)

	req = requests.get(page)
	text = req.text.encode('utf-8')

	siteObj = BeautifulSoup(text, 'html.parser')

	response = siteObj.find_all("div", {"class":"sense"})
	response = str(str(response).encode("utf-8"))

	clean_response = cleanhtml(response)
	da = " ".join(clean_response.split())

	da = da.replace("\\n", '')
	print(da)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Input a word to search for its definition.\nEg: dict abbveviation")
		sys.exit(0)

	import re
	import requests
	from bs4 import BeautifulSoup
	
	main()
