"""
This example script will retrieve the whole list of urls visible in a target url
"""

from urllib.request import urlopen
import re

target_url = "https://elcomercio.pe/"

website = urlopen(target_url)

html = website.read().decode('utf-8')

patt = '((http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))' \
       '([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)'
links = re.findall(patt, html)

link_list = []

for url in links:
    link_list.append(url[0])

f = open('link_list.txt', 'w')
f.write(str(link_list))
f.close()
