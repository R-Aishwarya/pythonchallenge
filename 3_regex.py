import urllib.request
import re
url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
text = str(url.read()).split('<!--')[-1].replace('-->','').replace('\n','')

print(re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',text))
