import urllib.request, json

import string
import argparse as ps 
parser=ps.ArgumentParser()
parser.add_argument('url',type=str,help='given url site')
args=parser.parse_args()
url=args.url
print(url)
#class Quiz:
    


response = urllib.request.urlopen(url)
soap=BeautifulSoup(response)
for link in soup.findAll('a'):
    print( link.get('href'))