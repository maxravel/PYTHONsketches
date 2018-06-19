# x = 6
# print(x/2)
# print(type(x))
# print(type(x/2))

# y = "hello"
# z = " world"
# print(y+z)
# print(type(y+z))

# p = input()
# p = int(p)
# #p = float(p)
#
# print(p*2)
# print(type(p*2))


# x = "asddfafdafads"
# x = x[1:4]
# print(x)

# x = 67
# if x == 5:
#     print("x jest inne")
# else:
#     print("jakie?")
# print("gotowe")
#
# x = 6 < 7
# print(x)
# print(type(x))
#
# y = 1
# print(bool(y))


# listy
# produkty = ["ser","mleko","parówki"]
# produkty.append("pomidor")
# print(produkty[1:2])
# print(type(produkty))
# # produkty.clear()
# print(produkty)
# x = produkty.count("pomidor")
# print(x)
# wiecej_produktow = ["kawa","sos"]
# produkty.extend(wiecej_produktow)
# produkty.pop(0)
# produkty.remove("sos")
# print(produkty)


# tuple nie można edytować
# przybory = ("dlugopis","linijka","kredka")
# print(przybory)


# słowniki
# person = {"wiek":20,"imię":"ania","nazwisko":"kowalska"}
# print(person)
# print(person["wiek"])
# keys = person.keys()
# print(keys)

# pętla while
# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# print("koniec")

# i=10
# while i>0:
#     print(i)
#     i -= 1
# print("koniec")

# suma = 0
# while True:
#     print("wpisz liczbę")
#     x = input()
#     suma += int(x)
#     print(suma)

# lista = ["a","b","c","d","e","f","g"]
#
# for litera in lista:
#     print(litera)
#     if litera == "e":
#         print("to jest e!")

# for i in range(10,30,2):
#     print(i)

# fruits = ["apple", "pear", "banana", "orange", "apple"]
# first one is enumerating number:
# for i, fruit in enumerate(fruits):
#     print("Sprawdzam {}".format(i))
#     if i == 3:
#         break
#     print(i)
#     print(fruit)
# print("koniec")

# x = "Hello {}"
# y = x.format("world!")
# print(y)

# fruits = ["bee", "pear", "banana", "orange", "strawberry"]
# for fruit in fruits:
#     if fruit == "pear": continue
#     print(fruit)
#     if fruit == "banana": break

# fruits = ["bee", "pear", "banana", "orange", "strawberry"]
# if "apple" in fruits:
#     print("znaleziono jabłko")
# elif "orange" in fruits:
#     print("nie znaleziono jabłka, ale mamy pomarańczę")
# else:
#     print("nic nie znaleziono")


# while True:
#     liczba = int(input())
#     if liczba > 20 and liczba < 80:
#         print("liczba jest większa od 20, ale mniejsza od 80")
#     elif liczba >100 or liczba > 80:
#         print("liczba jest większa od 100 lub od 80")
#     else:
#         print("nic")


# import time
# print("Start")
# time.sleep(2)
# # stop pojawi się po 2 sekundach
# print("Stop")

# timer = time.time()
# time.sleep(2)
# d = time.time() - timer
# print(d)

# timer = time.time()
# timer2 = time.time()
# timer3 = time.time()
# while True:
#     if time.time() - timer > 2:
#         print("minelo 2 sekundy")
#         timer = time.time()
#     if time.time() - timer2 >1:
#         print("minela 1 sekunda")
#         timer2 = time.time()
#     if time.time() - timer3 >5:
#         break

# import datetime
# teraz = datetime.datetime.now()
# print(str(teraz.hour)+" : "+str(teraz.minute))
# print(str(teraz.strftime("%H:%M  %d.%m.%Y")))


# def printme(liczba):
#     print("hello")
#     print(liczba)
#
# printme(5)

# def mnoz(a,b=4):
#     return a*b
# 
# wynik = mnoz(2)
# 
# print(wynik)



# # import file
# import new
# new.test("hello")
# new.test("121")

# # import function from file
# from new import test
# test("hello")
# test("121")

# # import all from file
# from new import *
# test("another one")

# def testOne():
#     print("Test one run.py")

# # import function with same name as another name
# from new import testOne as testOneNew
# testOne()
# testOneNew()



# files, tribes
# r - read, r+ - read+write, w - also create, w+, a, a+
# f = open("plik.txt","w")
# f.write("test1")
# f.close()
# \n - write in new line

# f = open("plik.txt","r")
# # print(f.read())
# # print(f.readlines())
# print(f.readline())
# f.close()

# f = open("plik.txt","r")
# for line in f.readlines():
#     print(line)
# f.close()



# # folders
# import os
# lista = os.listdir(".")
# print(lista)
#
# for item in os.listdir("."):
#     # print(item)
#     if os.path.isfile(item):
#         # .format put in curly braces item from ()
#         print("{} is a file".format(item))
#     elif os.path.isdir("."):
#         print("{} is a folder".format(item))
#     else:
#         print("{} is not a folder or file".format(item))

# # creating folder
# import os
# os.mkdir("newFolder")

# # rename folder
# os.rename("newFolder","bestFolder")

# # remove directory - os.rmdir("directory"); remove file - os.remove("file")
# os.rmdir("bestFolder")

# open("test2.txt","w").close()


# # making directories
# import os
# path="pliki/11/data.txt"
# print(os.path.dirname(path))
# print(os.path.basepath(path))
# print(os.path.abspath(path))
# os.makedirs(os.path.dirname(path))
# open(path,"w").close()




#exceptions

# try:
#     file = open("tekst.txt","r+")
#     file.write("tester")
#     file.close()
# # if file can't be created exception works:
# except FileNotFoundError as e:
#     print("wystąpił błąd z plikiem")
#     print(e)
#
# try:
#     file2 = open("plik.txt","r")
#     file2.write("xero")
#     file.close()
# except FileNotFoundError as e:
#     print("wystąpił błąd z plikiem")
#     print(e)
# except:
#     print("some other error")



# # objects
# class Calculator():
#     def __init__(self):
#         print("init")
#         #declaring self parametr
#         self.liczba=10
#     def __del__(self):
#         print("del")
#     def __str__(self):
#         return "hello"
#     def __len__(self):
#         return 6
#     def __bool__(self):
#         return False
#     def dodaj(self, a, b):
#         wynik = a+b
#         print(wynik)
#     def odejmij(self, a, b):
#         wynik = a-b
#         print(wynik)

# my_calculator = Calculator()
#
# my_calculator.dodaj(2,3)

# test = Calculator()
# # this del deletes test variable:
# del test
# print(test)

# test3 = Calculator()
# test3.dodaj(3,3)
# # this prints hello (__str__) when converting to string
# print(test3)

# if test3:
## __bool__ store boolean value of class
#     print("True")
# else:
#     print("Falseeee")

# calc = Calculator()
# calc.liczba = 10
# calc.liczba+=5
# print(calc.liczba)
#
# calc2 = Calculator()
# calc2.liczba+=5
# print(calc2.liczba)

# class Calculator2:
#     def __init__(self):
#         self.ostatni_wynik = 0
#
#     def dodaj(self, a, b):
#         wynik = a+b
#         self.ostatni_wynik = wynik
#         print(wynik)
#     def odejmij(self, a, b):
#         wynik = a - b
#         self.ostatni_wynik = wynik
#         print(wynik)
#
# calc21 = Calculator2()
# calc21.dodaj(3,2)
# calc21.dodaj(10,5)
# calc21.odejmij(17,9)
# print("Ostatni wynik:{}".format(calc21.ostatni_wynik))