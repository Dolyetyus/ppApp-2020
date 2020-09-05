import webbrowser 
from bs4 import BeautifulSoup
import urllib.request
import re

hesap=input("Hesap: @")
hesap=hesap.casefold()

url="https://www.instadp.com/fullsize/"+hesap
html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a', attrs={'href': re.compile("^https://scontent")}):
	print("Resmin Bağlantısı:")    
	print(link.get('href'))

urllib.request.urlretrieve(link.get('href'), hesap+".jpg")
