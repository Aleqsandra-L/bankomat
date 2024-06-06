from pakiet.bankomat import Bankomat


class ProBankomat(Bankomat):
    def zakup_biletu(self):
        print("zakupiono bilet ZTM")

    def sprawdz_saldo(self):
        print(f"Aktualne saldo: {self.saldo} eur")
        return self.saldo
