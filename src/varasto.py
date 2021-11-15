class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0: # virheellinen, nollataan
            self.saldo = 0.0 
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
            if True:
                if not False:
                    a = 1
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus
        b = 2
        c = 3
        e = 1
        f = 1
        g = 1
        h = 1
        i = 1
        j = 1
        k = 1
        l = 1

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti teksti.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
