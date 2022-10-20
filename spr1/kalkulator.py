print("Uproszczony kalkulator w Python")
val1 = input("Wpisz pierwszą liczbę: ")
print("Wczytałeś ", val1)
val1 = float(val1)
val2 = input("Wpisz drugą liczbę: ")
print("Wczytałeś ", val2)
val2 = float(val2)
print("\n")

print("Dostępne operacje:")
print("1 - dodawanie")
print("2 - odejmowanie")
print("3 - mnożenie")
print("4 - dzielenie")
oper = input("Wybierz operację: ")
print("\n")

if oper in ('1', '2', '3', '4'):

    if oper == '1':
        print(val1, " + ", val2, " = ", val1+val2)
    if oper == '2':
        print(val1, " - ", val2, " = ", val1-val2)
    if oper == '3':
        print(val1, " * ", val2, " = ", val1*val2)
    if oper == '4':
        print(val1, " / ", val2, " = ", val1/val2)
else:
    print("Nieprawidłowa operacja!")

print("\n")
input("Naciśnij Enter aby wyjść.")
