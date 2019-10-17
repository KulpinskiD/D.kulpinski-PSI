def main():
    #cw1
    lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
    #cw2
    print("cw2===============================================================")
    imie="Dawid"
    nazwisko="Kulpinski"
    litery_imie=imie.count(imie[2])
    litery_nazwisko = nazwisko.count(nazwisko[3])
    print("w tekscie jest "+ str(litery_imie) +imie[2]+ str(litery_nazwisko)+nazwisko[3] )
    #cw 3
    print("cw3===============================================================")
    print('{} {}'.format('jeden', 'dwa'))
    print('{:>2}'.format('test'))
    print('{:>12}'.format('test2'))
    print('{:07d}'.format(17))
    print('{jeden} {dwa}'.format(jeden='ala', dwa='kota!'))
    #cw 4
    print("cw4===============================================================")
    #print(dir(imie))
    #help(imie.islower())
    #cw 5
    print("cw5===============================================================")
    a=imie[::-1]
    b=nazwisko[::-1]
    print(a,b)
    #cw 6
    print("cw6 i cw7===============================================================")
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
    print("cw8===============================================================")
    student1=(1,"Jan","Kowalski")
    student2=(2,"Dawid","Kulpiński")
    student3=(3,"Adam","Nowak")
    lista_studentów=student1,student2,student3
    print(lista_studentów)
    #cw 9
    print("cw9===============================================================")
    #cw 10
    print("cw10===============================================================")
    lista_telefony=[111111111,111111112,111111111,111111113,111111114,111111111]
    lista_telefony.sort()
    usuwany=0
    b=0
    for x in lista_telefony:
        if lista_telefony[b] == lista_telefony[b+1]:
            usuwany = lista_telefony[b]
            lista_telefony.remove(usuwany)
        b+1
    print(lista_telefony)
    #cw11
    print("cw11===============================================================")
    liczby_od_0_do_10=range(11)
    for n in liczby_od_0_do_10:
        print(n)
    #cw12
    print("cw12===============================================================")
    liczby_od_100_do_20=range(100,-25,-5)
    for n in liczby_od_100_do_20:
        print(n)
    #cw13
    print("cw13===============================================================")

main()