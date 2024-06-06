
class Bankomat:
    def __init__(self, poczatkowe_saldo=0):
        self.saldo = poczatkowe_saldo

    def wplata(self, kwota):
        if kwota >0:
            self.saldo += kwota
            print (f"Wpłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")
        else:
            print("Kwota musi byc wieksza od zera")

    def wyplata(self, kwota):
        if kwota>0:
            if self.saldo>= kwota:
                self.saldo -= kwota
                print (f"wypłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN")
            else:
                print("Niewystarczajace srodki")
        else:
            print("Kwota wypłaty musi byc wieksza od zera")

    def sprawdz_saldo(self):
        print(f"Aktualne saldo: {self.saldo} PLN")
        return self.saldo