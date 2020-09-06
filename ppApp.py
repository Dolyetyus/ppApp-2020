#MADE BY DOLYETYUS -THT

import os
import webbrowser 
from bs4 import BeautifulSoup
import urllib.request
import re
from colorama import Fore, Back, init

init(autoreset="true")

edit=0

def pp():
	while edit==0:
		print(Back.BLUE+ Fore.YELLOW+ "Profil Resmi İndirici")
		hesap=input("Hesap adını giriniz: @")
		hesap=hesap.casefold()
		print()
		print(Fore.YELLOW+ "@" +hesap+ " adlı kişinin profil resmini indireceksiniz. \nHesap adını değiştirmek için [0]\nDevam etmek için herhangi bir tuşuna basın")

		try:	
			düzenle=int(input())
			print()
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
				print(Fore.GREEN+ "Kullanıcının profil resmi, uygulamanın bulunduğu dizine indirilmiştir")   
				link.get('href')
	
			urllib.request.urlretrieve(link.get('href'), hesap+".jpg")
			break

		except UnboundLocalError:
			url="https://www.instadp.com/fullsize/"+hesap
			html_page = urllib.request.urlopen(url)
			soup = BeautifulSoup(html_page, "html.parser")
			for link in soup.findAll('a', attrs={'href': re.compile("^https://instagram")}):
				print(Fore.GREEN+ "Kullanıcının profil resmi, uygulamanın bulunduğu dizine indirilmiştir")
				print(Back.RED+ "Instagram kaynaklı olarak indirilen resim FULL HD çözünürlüğünde değildir!")   
				link.get('href')
	
			urllib.request.urlretrieve(link.get('href'), hesap+".jpg")
			break

		except:
			print(Fore.RED+ "HATA: Instagram hesabı veya profil resmi bulunamadı \n")
			break 

	
def story():
	while edit==0:
		print(Back.BLUE+ Fore.YELLOW+ "Hikaye İndirici")
		hesap=input("Hesap adını giriniz: @")
		hesap=hesap.casefold()
		print()
		print(Fore.YELLOW+ "@" +hesap+ " adlı kişinin son paylaştığı hikayeyi indireceksiniz. \nHesap adını değiştirmek için [0] \nDevam etmek için herhangi bir tuşuna basın")

		try:	
			düzenle=int(input())
			print()
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
			url="https://www.instadp.com/stories/"+hesap
			html_page = urllib.request.urlopen(url)
			soup = BeautifulSoup(html_page, "html.parser")
			for link in soup.findAll('a', attrs={'href': re.compile("^https://scontent")}):   
				link.get('href')

			print("Hesabın son paylaştığı hikaye fotoğraf ise [1]\nHesabın son paylaştığı hikaye video ise [2]:")
			print("(GIF veya InstaMusic içeren storyler de video kabul edilmektedir,\nDosya biçimini yanlış seçerseniz, indirilen dosya açılmaz)")
			save=int(input())

			if save==2:
				urllib.request.urlretrieve(link.get('href'), hesap+".mp4")
				print(Fore.GREEN+ "Hikaye, video olarak kaydedildi")
				break

			elif save==1:
				urllib.request.urlretrieve(link.get('href'), hesap+".png")
				print(Fore.GREEN+ "Hikaye, resim olarak kaydedildi")
				break
		except UnboundLocalError:
			print(Fore.RED+ "HATA: Instagram hesabı gizli veya hikaye bulunamadı \n")
			break 
	
while True:
	os.system('cls')  
	os.system('clear')

	print(Fore.BLUE+ "*" *40)
	print(Fore.BLUE+ "*                                      *")
	print(Back.YELLOW+ Fore.BLACK+ "* INSTAGRAM PROFIL PICTURE DOWNLOADER  *")
	print(Fore.BLUE+ "*                                      *")
	print(Fore.BLUE+ "*" *40)

	islem=int(input("Bir hesabın profil resmini indirmek için [1]\nBir hesabın son hikayesini indirmek için [2]: "))
	print()
	if islem==1:
		pp()
	elif islem==2:
		story()

	
	print()
	print(Fore.YELLOW+ "Ana menüye dönüş yapmak için [1] \nUygulamadan çıkış yapmak için [0]: ")
	con=int(input())
	
	if con==1:
		continue
	elif con==0:
		break
	else:
		print(Fore.RED+ "Yanlış bir komut girdiniz. Çıkış yapılıyor...")
		break

print(Fore.RED+ Back.GREEN+ "Çıkış yapmak için herhangi bir tuşa basın")
print(Fore.GREEN+ "Dolyetyus, 2020")
input()
