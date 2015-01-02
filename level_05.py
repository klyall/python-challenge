from common import loadPageAndExtractText, openNextPage
import urllib2, pickle

pickle_file = loadPageAndExtractText("peak", r'<peakhell src="(.*?)"/>')

# Load pickle file reference in page
page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/%s" % (pickle_file, ))
banner = pickle.load(page)

# Print ascii art
for row in banner:
	print "".join(i[0] * i[1] for i in row)

openNextPage("channel")
