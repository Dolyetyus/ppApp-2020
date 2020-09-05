#MADE BY DOLYETYUS -THT

import os
import webbrowser 
from bs4 import BeautifulSoup
import urllib.request
import re
from colorama import Fore, Back, init

init(autoreset="true")

edit=0

def download():
	while edit==0:
		hesap=input("Hesap adını giriniz: @")
		hesap=hesap.casefold()
		print()
		print(Fore.YELLOW+ "@" +hesap+ " adlı kişinin profil resmini indireceksiniz. \nHesap adını değiştirmek için 0'a basın \nDevam etmek için herhangi bir tuşuna basın")
		
		try:	
			düzenle=int(input())
		except ValueError:
			düzenle=1
		if düzenle==0:
			continue
			os.system('cls')  
			os.system('clear')
		elif düzenle==1:
			break		
		else:
			break
	
	while True:
		try:
			url="https://www.instadp.com/fullsize/"+hesap
			html_page = urllib.request.urlopen(url)
			soup = BeautifulSoup(html_page, "html.parser")
			for link in soup.findAll('a', attrs={'href': re.compile("^https://scontent")}):
				print(Fore.RED+ "Kullanıcının profil resmi, uygulamanın bulunduğu dizine indirilmiştir")
				print("İsteyenler İçin Resmin Bağlantısı:")    
				print(link.get('href'))
	
			urllib.request.urlretrieve(link.get('href'), hesap+".jpg")
			break

		except UnboundLocalError:
			print(Fore.RED+ "HATA: Instagram hesabı veya profil resmi bulunamadı \n")
			break 
		

while True:
	os.system('cls')  
	os.system('clear')
  
	print(Fore.RED+ "*" *40)
	print(Back.YELLOW+ Fore.BLACK+ "INSTAGRAM PROFIL PICTURE DOWNLOADER")
	print(Fore.RED+ "*" *40)
	
	download()
	
	print()
	print(Fore.YELLOW+ "Uygulamayı yeniden Kullanmak için 1'e basınız \nUygulamadan çıkış yapmak için 0'a basınız:")
	con=int(input())
	
	if con==1:
		continue
	elif con==0:
		break
	else:
		print(Fore.RED+ "Yanlış bir komut girdiniz. Çıkış yapılıyor...")
		break

print(Fore.GREEN+ "Dolyetyus, THT, 2020")
print(Fore.RED+ Back.GREEN+ "Çıkış yapmak için herhangi bir tuşa basın")
input()

