#deneme-start
sayiListesi=[]
for i in range(10):
  sayi=int(input(("sayi giriniz")))
  sayiListesi.append(sayi)
print(sayiListesi)

enkucuk=min(sayiListesi)
enbuyuk=max(sayiListesi)
print(f'Girilen en kucuk deger: {enkucuk}')
print(f'Girilen en buyuk deger: {enbuyuk}')

for sorting in range(0,enbuyuk,2): #en büyük sayiya kadar olan çift sayiları siralama
     print(sorting)



ustLimit=int(input("Ust limit giriniz"))
altLimit=int(input("Alt limit giriniz"))

if i in range(altLimit,ustLimit,2):
    print(i)
    



#Sinem

    numbers = []  #  bos bir liste olusturduk.
for i in range(10):
    num = int(input("Sayi Giriniz: ")) #kullanıcıdan veri istedik.
    numbers.append(num) #aldığımız veriyi diziye ekledik append() komutu bunun için kullanıldı, listenin sonuna yeni ögeyi ekler.
print(numbers)

smallNum = min(numbers) # en küçük sayı
biggestNum = max(numbers) # en büyük sayma

print(f'Girilen En Küçük Değer: {smallNum}') # en küçük değer.
print(f'Girilen En Büyük Değer: {biggestNum}') # en büyük değer.

# 0 dan başlayıp en büyük sayıya kadar olan çift sayıları yazdırdık.
for evenNum in range(0,biggestNum,2):  # 0 dan başlattığımız için çift mi tek mi bakmamıza gerek yok.
        print(evenNum)


# alt limit belirleyip listemizdeki üst limite kadar ikişer saydırdıık.
upNum= int(input("Alt limit giriniz: "))
num2 = int(input("Alt limit belirlemek için 1 giriniz: ")) #saydırma işlemi için alt taban belirledik.
if num2 == 1:
     for i in range(upNum, biggestNum, 2):
          print(i)
else:
     print("Geçersiz bir giriş yapildi.")
