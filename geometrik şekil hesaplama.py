def geometri(sekil):
    if len(sekil) == 3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a+b > c) and (a+c > b) and (b+c > a):
            if (a == b) and (a == c) and (b == c):
                print("Eşkenar Üçgen")

            elif ((a == b) and (a != c)) or ((a == c) and (a != b)):
                print("İkizkenar Üçgen")

            else:
                print("Çeşitkenar Üçgen")

        else:
            print("Üçgen oluşturulamaz!")


    if len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if (a == b) and (a == c) and (a == d):
            print("Kare")

        elif ((a == b) and (c == d) and (a != c)) or ((a == c) and (b == d) and (a != b)) or ((a == d) and (b == c) and (a != b)):
            print("Dikdörtgen")

        else:
            print("Özel dörtgen oluşturulamaz")

while (True):
    elemanSayisi = int(input("Eleman sayısı giriniz :"))

    if (elemanSayisi == 3):
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))

        geometri([a, b, c])

    elif (elemanSayisi == 4):
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))
        d = int(input("d ="))

        geometri([a, b, c, d])

    else:
        print("Geçerli eleman sayısı giriniz.")