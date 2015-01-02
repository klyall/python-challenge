from common import loadPageAndExtractText, openNextPage
import re

text = loadPageAndExtractText("equality", r'<!--(.*?)-->')

pattern2 = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', re.DOTALL)
result =  pattern2.findall(text)

name = "".join(result)

openNextPage(name)
