def main():
    #cw1
    lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
    #cw2
    imie="Dawid"
    nazwisko="Kulpinski"
    litery_imie=imie.count(imie[2])
    litery_nazwisko = nazwisko.count(nazwisko[3])
    print("w tekscie jest "+ str(litery_imie) +imie[2]+ str(litery_nazwisko)+nazwisko[3] )
    #cw 3
    print('{} {}'.format('jeden', 'dwa'))
    print('{:>2}'.format('test'))
    print('{:>12}'.format('test2'))
    print('{:07d}'.format(17))
    print('{jeden} {dwa}'.format(jeden='ala', dwa='kota!'))
    #cw 4
    #print(dir(imie))
    #help(imie.islower())
    #cw 5
    a=imie[::-1]
    b=nazwisko[::-1]
    print(a,b)
    #cw 6
    lista=[1,2,3,4,5,6,7,8,9,10]
    lista2=[]
    #cw 7
    lista3=[]
    for x in lista[5::]:
        lista2.append(x)
        lista.pop()
    lista3=lista+lista2
    lista3.insert(0,0)
    lista3=lista3[::-1]
    print(lista3)
    #cw8
studencji = (1, "Jan", "Nowak",2, "Jan", "Kowalski",3,"")




main()