class Colibri:
    def __init__(self, espècie, mida, edat, velocitat, color):
        self.espècie = espècie
        self.mida = mida
        self.edat = edat
        self.velocitat = velocitat
        self.color = color

    # Getters
    def get_espècie(self):
        return self.espècie

    def get_mida(self):
        return self.mida

    def get_edat(self):
        return self.edat

    def get_velocitat(self):
        return self.velocitat

    def get_color(self):
        return self.color

    # Setters
    def set_espècie(self, espècie):
        self.espècie = espècie

    def set_mida(self, mida):
        self.mida = mida

    def set_edat(self, edat):
        self.edat = edat

    def set_velocitat(self, velocitat):
        self.velocitat = velocitat

    def set_color(self, color):
        self.color = color
