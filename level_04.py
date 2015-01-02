from common import loadPage, openNextPage
import urllib2
import re

pattern = re.compile(r'next nothing is ([\d]+)', re.DOTALL)

number = 12345
cont = True

while cont:
	page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % (number, ))
	body = page.read()
	result =  pattern.search(body)
	if result:
		number = result.groups()[0]
		print number
	elif body == "Yes. Divide by two and keep going.":
		number = int(number) / 2
		print number
	else:
		name = body
		cont = False
		print name

openNextPage(name)
