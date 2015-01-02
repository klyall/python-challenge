from common import loadPageAndExtractText, openNextPage
from string import maketrans

currentPage = "map"
text = loadPageAndExtractText(currentPage, r'<font color="#f000f0">(.*?)</tr></td>')

# Translate the message
intab  = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

print text.translate(trantab);

nextPage = currentPage.translate(trantab)

openNextPage(nextPage)
