# Python program to read 
# image using PIL module 
  
# importing PIL
import io
from urllib.request import urlopen
import json
from PIL import Image 

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
# Read image 
img = Image.open(io.BytesIO(urlopen(url).read()))
pix_val = list(img.getdata())
width, height = img.size
ans = ''
# r,g,b, same for a grayscale image
for elt in pix_val:
    same_tup = tuple((elt[0],)*3)
    if elt[:3] == same_tup:
        ans += chr(elt[0])
i = ans.find('[')
j = ans.find(']')
final_ans = json.loads(ans[i:j+1:7])
print(final_ans)
print([chr(i) for i in final_ans])

"""
Check answers at http://www.pythonchallenge.com/pcc/def/integrity.html
"""