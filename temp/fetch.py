import urllib2
from BeautifulSoup import BeautifulSoup

src = urllib2.urlopen('http://www.amazon.com/George-F-Kennan-American-Life/dp/1594203121/ref=amb_link_359769522_5?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=0NXCXBM9BA5AXRWGQ51T&pf_rd_t=101&pf_rd_p=1350587622&pf_rd_i=283155')
parser = BeautifulSoup(src)
title_p = parser.find('span', {'id':'btAsinTitle'})
title = title_p.contents[0]
print title

