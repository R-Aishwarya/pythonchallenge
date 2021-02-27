import zipfile
import os
import io
from urllib.request import urlopen
url = "http://www.pythonchallenge.com/pc/def/channel.zip"
curr_dir = os.path.dirname(__file__)
zip_ref = zipfile.ZipFile(io.BytesIO(urlopen(url).read()),'r')
zip_ref.extractall(curr_dir + '/channel')

next_file = 90052
ans = ''
while(True):
    with open(curr_dir + '/channel/' + str(next_file)+'.txt') as f:
        content = f.read()
        if content.startswith('Next nothing is '):
            next_file = content.split('Next nothing is ',1)[1]
            ans += zip_ref.getinfo(str(next_file)+'.txt').comment.decode()
        elif content == "Collect the comments.":
           print(ans)
           break


"""
Check answers at http://www.pythonchallenge.com/pcc/def/oxygen.html
"""