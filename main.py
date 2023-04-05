baslik="Haberiniz Olsun"
vade=12
faizorani=1.47

# typing-start
print(type(baslik))
print(type(vade))
# typing-end


# karşılama-start
mesaj="Hoşgeldin"
MüsteriAdi="Methiye"
MüsteriSoyadi="Şahin Taş"
sonucmesaj=mesaj + " " +MüsteriAdi+" " +MüsteriSoyadi
print(sonucmesaj)
# karşılama-end

sayi1=10
sayi2=20
print(sayi1+sayi2)

krediler = ["Hizli Kredi","Maaşini Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
print(krediler)    #kredilistele
print(krediler[0]) 
print(krediler[1]) 
print(krediler[2]) 
print(len(krediler))

krediler[0]="Çabuk kredi" #listedeki ögeyi güncelleme
print(krediler)
print(krediler[2])

krediler = ["Hizli Kredi","Maaşini Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]

for kredi in krediler:  #kendi içinde döngü
    print(kredi)

for i in range(3,10):
    print(i)

for i in range(0,11,2):  #0 dan 11 e kadar sayılar 2 şer artırarak sırala
    print(i)

def krediListele():  #fonksiyon
  krediler = ["Hizli Kredi","Maaşini Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
  for kredi in krediler:
    
    print("<option>"+kredi+"<option>")

krediListele()

