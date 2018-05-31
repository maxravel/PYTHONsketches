# x = 6
# print(x/2)
# print(type(x))
# print(type(x/2))
#
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


