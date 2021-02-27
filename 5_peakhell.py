import urllib.request
import pickle
import json
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
text = urllib.request.urlopen(url).read()
data = pickle.loads(text)
for elt in data:
    stri = ''
    for tup in elt:
        stri += tup[0] * tup[1]
    print(stri)


"""
Check answers at http://www.pythonchallenge.com/pcc/def/channel.html
"""