class Cotxe:
    def __init__(self, marca, model, any, color, preu):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.preu = preu

    # Getters
    def get_marca(self):
        return self.marca

    def get_model(self):
        return self.model

    def get_any(self):
        return self.any

    def get_color(self):
        return self.color

    def get_preu(self):
        return self.preu

    # Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_model(self, model):
        self.model = model

    def set_any(self, any):
        self.any = any

    def set_color(self, color):
        self.color = color

    def set_preu(self, preu):
        self.preu = preu
