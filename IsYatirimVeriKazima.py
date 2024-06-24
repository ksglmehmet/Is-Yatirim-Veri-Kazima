import requests
from bs4 import BeautifulSoup
import time
import re

class Hisse:
    def __init__(self):
        self.dongu = True
    
    def program(self):
        
        secim = self.menu()
        
        if secim == "1":
            print("Güncel Fiyatlar Alınıyor...\n")
            time.sleep(3)
            self.guncelfiyat()
        if secim == "2":
            print("Künye Bilgileri Alınıyor...\n")
            time.sleep(3)
            self.kunye()
        if secim == "3":
            print("Cari Değerler Alınıyor...\n")
            time.sleep(3)
            self.carideger()
        if secim == "4":
            print("Getiri Bilgileri Alınıyor...\n")
            time.sleep(3)
            self.getiri()
        if secim == "5":
            print("Endeks Ağırlık Oranları Alınıyor...\n")
            time.sleep(3)
            self.dahilendeks()
        if secim == "6":
            print("Otomasyondan Çıkılıyor Teşekkürler.")
            time.sleep(3)
            self.cikis()
    
    def menu(self):
        
        def kontrol(secim):
            if not re.search("[1-6]", secim):
                raise Exception("Lütfen 1 ve 6 değerler arasında geçerli bir seçim yapınız.")
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ve 6 değerler arasında geçerli bir seçim yapınız.")
        
        while True:
            try:
                secim = input("Merhaba, Anlaşılır Ekonomi Otomasyon Sistemine Hoşgeldiniz...\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1]-Güncel Fiyatlar\n[2]-Şirket Künyesi\n[3]-Cari Değerler\n[4]-Getiri Rakamları\n[5]-Şirketin Dahil Olduğu Endeksler\n[6]-Çıkış\n\n")
                kontrol(secim)
            except Exception as Hata:
                print(Hata)
                time.sleep(3)
            else:
                break
        return secim

    
    def guncelfiyat(self):
        
        while True:
            try: # Kişinin gireceği hisse senedi kodu yok ise hata döndüreceğim.
                sirket = input("Lütfen Şirket Adı Giriniz: ")
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"
                parser = BeautifulSoup(requests.get(url).content, "html.parser")
                fiyat = parser.find("a", {"href": "/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket.upper())}).parent.parent.find_all("td") # Bu etkiketten önceki etikete geçeceğim. Child.
                Isim = fiyat[0]["title"].strip()
                SonFiyat = fiyat[1].text
                DegisimYuzde = fiyat[2].span.text.strip()
                DegisimTL = fiyat[3].text
                HacimTL = fiyat[4].text
                HacimAdet = fiyat[5].text
                print(f"\nŞirket İsmi: {Isim}\nSon Fiyat: {SonFiyat}\nDeğişim(%): {DegisimYuzde}\nDeğişim(TL): {DegisimTL}\nHacim TL: {HacimTL}\nHacim Adet: {HacimAdet}\n")
                break
            except AttributeError:
                print("Hatalı bir şirket adı girdiniz...")
                time.sleep(1)
        time.sleep(3)
        self.menudon()
                
    def kunye(self):
        
        while True:
            try: # Kişinin gireceği hisse senedi kodu yok ise hata döndüreceğim.
                sirket = input("Lütfen Şirket Adı Giriniz: ")
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={sirket}"
                parser = BeautifulSoup(requests.get(url).content, "html.parser")
                Kunye = parser.find("div", {"id": "ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"}).find_all("tr") # parser ile liste haline çeviriyoruz.
                for i in Kunye:
                    Bilgi1 = i.th.text
                    Bilgi2 = i.td.text
                    print(f"{Bilgi1}: {Bilgi2}")
                break
            except AttributeError:
                print("Hatalı bir şirket adı girdiniz...")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def carideger(self):
        
        while True:
            try: # Kişinin gireceği hisse senedi kodu yok ise hata döndüreceğim.
                sirket = input("Lütfen Şirket Adı Giriniz: ")
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={sirket}"
                parser = BeautifulSoup(requests.get(url).content, "html.parser")
                CariDeger = parser.find("div", {"id": "ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"}).find_all("tr") # parser ile liste haline çeviriyoruz.
                for i in CariDeger:
                    Bilgi1 = i.th.text
                    Bilgi2 = i.td.text
                    print(f"\n{Bilgi1}: {Bilgi2}")
                break
            except AttributeError:
                print("Hatalı bir şirket adı girdiniz...")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def getiri(self): # Tablo yatay ve dikey, biraz daha farklı.
        
        while True:
            try: # Kişinin gireceği hisse senedi kodu yok ise hata döndüreceğim.
                sirket = input("Lütfen Şirket Adı Giriniz: ")
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={sirket}"
                parser = BeautifulSoup(requests.get(url).content, "html.parser")
                Getiri = parser.find("div", {"id": "ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}).find("table").find("tbody").find_all("tr")
                
                for i in Getiri:
                    Bilgi = i.find_all("td")
                    print(f"\nBirim: {Bilgi[0].text}\nGünlük(%): {Bilgi[1].text}\nHaftalık(%): {Bilgi[2].text}\nAylık(%): {Bilgi[3].text}\nYıl İçi Getiri(%): {Bilgi[4].text}")
                break
            except AttributeError:
                print("Hatalı bir şirket adı girdiniz...")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def dahilendeks(self):
        
        while True:
            try: # Kişinin gireceği hisse senedi kodu yok ise hata döndüreceğim.
                sirket = input("Lütfen Şirket Adı Giriniz: ")
                url = f"https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={sirket}"
                parser = BeautifulSoup(requests.get(url).content, "html.parser")
                DahiliEndeks = parser.find("div", {"id": "ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("tbody").find("tr").find_all("td")
                DahiliEndeks2 = parser.find("div", {"id": "ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("thead").find("tr").find_all("th")
                
                for i in range(0,3):
                    print(f"\n{DahiliEndeks2[i].text}: {DahiliEndeks[i].text}\n")
                break  
            except AttributeError:
                print("Hatalı bir şirket adı girdiniz...")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def cikis(self):
        
        print("Uygulamadan Çıkış Yapılmaktadır. İyi Günler.")
        time.sleep(1)
        self.dongu = False
        exit()
    
    def menudon(self):
        
        while True:
            x = input("\nAna Menüye Dönmek İçin 6'ye,\nTekrar Fiyat Sorgusu Yapmak için  7'ye,\nÇıkış Yapmak İçin Lütfen 8'ya Basınız...\n\n")
            if x == "6":
                print("Ana Menüye Dönülüyor...\n")
                time.sleep(3)
                self.program()
                break
            
            elif x == "7":
                time.sleep(3)
                self.guncelfiyat()
                break
            
            elif x == "8":
                time.sleep(2)
                self.cikis()
                break
            
            elif not re.search("[6-8]", x) or len(x) != 1:
                print("Lütfen Geçerli Bir Seçim Yapınız.")
 
Sistem = Hisse()
while Sistem.dongu:
    Sistem.program()