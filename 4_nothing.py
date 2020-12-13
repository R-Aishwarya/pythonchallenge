import urllib.request
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

strs = '16044'
for i in range(400):
    text = str(urllib.request.urlopen(url + strs).read())
    print(text)
    if 'Yes. Divide by two and keep going.' in text:
        strs = str(int(strs)/2)
    else:
        strs = text.split("and the next nothing is ",1)[1]
    print(strs)
