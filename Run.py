from pakiet.bankomat import Bankomat

print("Witam w programie")

# bankomat1 = Bankomat()
# bankomat1.sprawdz_saldo()
# bankomat1.wplata(1000)
# bankomat1.wyplata(400)

def multi(a,b):
    try:
        return a*b
    except TypeError:
        return 0

def multi2(a,b):
    try:
        return a*b
    except Exception as e:
        print(e)

def multi3(a,b):
    try:
        suma = a*b
    except TypeError:
        return 0
    except ValueError:
        return 1
    else:
        return suma
    finally:
        print("Działanie zostało zakończone")


print(multi(a= 5, b= 5))
print(multi2(a="5", b="tomek"))
print(multi3(a="5", b="tomek"))
print(multi3(a=5, b=6))