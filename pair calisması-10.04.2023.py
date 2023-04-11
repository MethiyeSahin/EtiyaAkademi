# Kullanıcıyı sürekli konsolda tutarak istediği kadar işlem yapmasını sağlayacak bir hesap makinesi programlayacağız. Hesaplama işlemlerinin her biri ayrı fonksiyon olmalıdır.
# Kullanıcı klavyeden ilk olarak istediği işlemi ( + - / * % ) girmelidir. Dört işleme ek mod hesaplama da dahil. Daha sonra gireceği iki sayının kullanıcının istediği işleme yönlendirilmesini eğer kullanıcıdan alınan değer yukarıdaki beş sembolden biri değilse programın hata vermesini sağlayalım. Kullanıcı işlem seçmek yerine “q” harfi girişi yaparsa programı sonlandıralım aksi takdirde program her hesaplama sonrası tekrar işlem yapabilir olmalıdır.


# PAİR KENDİ YAZDIĞIM
# def calculator():
    
#     sayi1=int(input("Bir sayi giriniz"))
#     sayi2=int(input("Bir sayi giriniz"))
#     islem=input("İslem seciniz")


#     if islem=="-":
#         print(sayi1-sayi2)
#     elif islem=="+":
#         print(sayi1+sayi2)
#     elif islem=="/":
#         print(sayi1/sayi2)
#     elif islem=="*":
#         print(sayi1/sayi2)
#     elif islem=='%':
#         print(sayi1/sayi2)
#     else:
#         print("Hatali islem girdiniz :( ")


# cikis = input("Çıkmak istiyorsanız 'q' basın.")
# while cikis != 'q':
#     calculator()
#     cikis = input("Çıkmak istiyorsanız 'q' basın.")


# PAİR
def calculator ():
    sayi1 = int(input("Bir sayı giriniz: "))
    sayi2 = int(input("Bir sayı giriniz: "))
    toplam = sayi1 + sayi2
    carpim = sayi1 * sayi2
    cikarma = sayi1 - sayi2
    bolme = sayi1 / sayi2
    mod = sayi1 % sayi2

    islem = input("İşlem seçiniz:")
    if islem == "+":
        print(toplam)
    elif islem == "-":
        print(cikarma)
    elif islem == "/":
        print(bolme)
    elif islem == "*":
        print(carpim)
    elif islem == "%":
        print(mod)
    else :
        print("Hatalı seçim")

cikis = input("Çıkmak istiyorsanız 'q' basın.")
while cikis != 'q':
    calculator()
    cikis = input("Çıkmak istiyorsanız 'q' basın.")