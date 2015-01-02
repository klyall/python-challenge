from common import loadPageAndExtractText, openNextPage

text = loadPageAndExtractText("ocr", r'<!--(\s+[%]+.*?)-->')
print text

#
# Solution 1
# Simplest code solution but inefficient as it counts the number of letters for every letter
#
#result1 = filter(lambda letter: message.count(letter) == 1, message)
#print result1

#
# Solution 2
# More code but computationally more efficient
#
counts = {}

# Count the number of letters once
for letter in text:
	if letter in counts:
		counts[letter] += 1
	else:
		counts[letter] = 1

# Filter out letters that only occur once in counted letters
letters = filter(lambda letter: counts[letter] == 1, counts.keys())

# Filter out letters from text that are in the rare letter list
result2 = filter(lambda letter: letter in letters, text)
print result2

openNextPage(result2)
