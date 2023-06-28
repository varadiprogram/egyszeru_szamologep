import math
import time

print("by: Váradi Zsolt")
print("")
print("⠀⠀⠀⠀     ⣀⣠⣤⣤⣶⣶⣶⣶⣶⣶⣠⣤⣤⣀⣀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⣀⣴⣾⠿⠟⠛⠛⠉⠉⠉⠉⠉⠛⠛⠛⠿⠿⡿⠛⢿⣿⣷⣤")
print("⠀⠀⠀⣠⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠉⠁")
print("⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠀⠀")
print("⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀")
print("⠋⠀⠀⠀⠀⠀ ⢀⣤⣤⣤⣶⣶⣆⢤⣤⣀⣀⠀⠀⠀⠀⣸⡟⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢸⡿⠋⠙⢿⣿⣿⣿⣻⣿⣿⡇⠀⠀⠀⣿⠇⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⠐⢻⣿⣻⣷⡽⣿⣷⠀⠀⢸⣿⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⠐⢻⣿⣻⣷⡽⣿⣷⠀⠀⢸⣿⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠿⣃⠹⠿⠗⣿⣷⣻⣿⡽⣿⣧⠀⣼⡇⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣴⡏⣁⢀⠲⣿⣿⣷⢻⣿⡽⣿⢀⣿⠁⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⣉⣡⣿⣿⣿⣏⣿⣿⣿⣼⡿⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢰⡿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⠛⠛⠆⠀⠀⠀⠀⠀")
print("  ⠀⠀⠀⠀⠀⠈⠛⠘⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("")
print("")
time.sleep(0.85)

elso_szam = float(input("első szám: "))
tenyezo = input("művelet: ")
masodik_szam = float(input("második szám: "))

vegeredmeny = None

time.sleep(0.3)


if tenyezo == "+":
    print("")
    print(elso_szam + masodik_szam)
    vegeredmeny = elso_szam + masodik_szam
    vegeredmeny = round(vegeredmeny)
    time.sleep(0.6)
    print("kerekítve: " + str(vegeredmeny))

elif tenyezo == "-":
    print("")
    print(elso_szam - masodik_szam)
    vegeredmeny = elso_szam - masodik_szam
    vegeredmeny = round(vegeredmeny)
    time.sleep(0.6)
    print("kerekítve: " + str(vegeredmeny))

elif tenyezo == "*":
    print("")
    print(elso_szam * masodik_szam)
    vegeredmeny = elso_szam * masodik_szam
    vegeredmeny = round(vegeredmeny)
    time.sleep(0.6)
    print("kerekítve: " + str(vegeredmeny))

elif tenyezo == "/":
    print("")
    print(elso_szam / masodik_szam)
    vegeredmeny = elso_szam / masodik_szam
    vegeredmeny = round(vegeredmeny)
    time.sleep(0.6)
    print("kerekítve: " + str(vegeredmeny))

else:
    print("nem értelmezhető szám vagy karakter")


elkosznoes = "Köszönöm hogy a programom használta"
print("")
for i in elkosznoes:
    print(i,end='')









