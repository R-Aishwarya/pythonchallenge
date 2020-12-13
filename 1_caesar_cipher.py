def decrypt(text, i):
    ans = ''
    for c in text:
        if c.isupper():
            ans = ans + chr(((ord(c) + i - 65) % 26) + 65)
        elif c.islower():
            ans = ans + chr(((ord(c) + i -97) % 26) + 97)
        else:
            ans = ans + c

    return ans

text = "http://www.pythonchallenge.com/pc/def/map.html"
print(decrypt(text, 2))

inp = 'abcdefghijklmnopqrstuvwxyz'
out = 'cdefghijklmnopqrstuvwxyzab'
tt = str.maketrans(inp,out)
print(text.translate(tt))