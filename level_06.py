from common import loadPageAndExtractText, openNextPage
import urllib2, re
from StringIO import StringIO
from zipfile import ZipFile

url = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

name = 'readme'
nextName = []

with ZipFile(StringIO(url.read()), 'r') as myzip:
	pattern = re.compile(r'([\d]{2,})', re.DOTALL)

	while True:
		readme = myzip.open("%s.txt" % (name, ), 'r')
		nextName.append(myzip.getinfo("%s.txt" % (name, )).comment)
		text = readme.read()
		print text
		result =  pattern.search(text)
		if result:
			name = result.groups()[0]
		else:
			name = text
			break

print "".join(nextName)

openNextPage('oxygen')
