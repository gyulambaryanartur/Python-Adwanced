
from urllib.request import urlopen
from html.parser import HTMLParser
respons=urlopen('https://aca.am/en/').read().decode()
html=respons.split('-->')[1].strip('\n<!--').split(' ')
a=""
for code in html:
    a+="".join(chr(int(code,2)))
print(a)    


