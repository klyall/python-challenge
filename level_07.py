from common import loadPageAndExtractText, openNextPage
import urllib2, re
from PIL import Image
from StringIO import StringIO

image_file = loadPageAndExtractText("oxygen", r'<img src="(.*?)"/>')

# Load image file referenced in page
url = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/%s" % (image_file, ))
img = Image.open(StringIO(url.read()))
#img = Image.open('oxygen.png')
pix = img.load()

width, height = img.size
lastPix = []
target_row = 0

# Find the stripe in the image
for y in range(0, height):
	currentPix = pix[0, y]
	if currentPix == lastPix:
		target_row = y
		break
	else:
		lastPix = currentPix

print "Stripe found at row %s" % (target_row, )

# Extract the red value from each block until grey blocks finish
values= []
lastPix = pix[0, target_row]
for x in range(0, width, 7):
	currentPix = pix[x, target_row]
	nextPix = pix[x + 1, target_row]
	if currentPix != lastPix and currentPix != nextPix:
		break
	else:
		r, g, b, x = currentPix
		values.append(r)
		lastPix = currentPix

message = "".join([chr(v) for v in values])
print message

# Extract numbers from message and convert into an array 
regex = re.compile(r'\[(.*?)\]', re.DOTALL)
result =  regex.search(message).groups()
numbers = result[0].split(", ")

# Convert array of numbers to characters
name = "".join([chr(int(v)) for v in numbers])

openNextPage(name)
