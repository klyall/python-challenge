import webbrowser, urllib2, re

def createURL(name, folder='def'):
	return "http://www.pythonchallenge.com/pc/%s/%s.html" % (folder, name)

def loadPage(name): 
	page = urllib2.urlopen(createURL(name))
	return page.read()

def loadPageAndExtractText(name, pattern): 
	page = loadPage(name)
	regex = re.compile(pattern, re.DOTALL)
	result =  regex.search(page).groups()
	return result[0]

def openNextPage(name, folder='def'):
	print "The next level is '%s'" % (name, )
	webbrowser.open(createURL(name, folder))
	src_url = "http://www.pythonchallenge.com/pcc/%s/%s.html" % (folder, name)
	webbrowser.open(src_url)
