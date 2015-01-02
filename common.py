import webbrowser, urllib2, re

def createURL(name):
	return "http://www.pythonchallenge.com/pc/def/%s.html" % (name, )

def loadPage(name): 
	page = urllib2.urlopen(createURL(name))
	return page.read()

def loadPageAndExtractText(name, pattern): 
	page = loadPage(name)
	regex = re.compile(pattern, re.DOTALL)
	result =  regex.search(page).groups()
	return result[0]

def openNextPage(name):
	webbrowser.open(createURL(name))
	src_url = "http://www.pythonchallenge.com/pcc/def/%s.html" % (name, )
	webbrowser.open(src_url)
