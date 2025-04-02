class Phalanx():
    def _init_(self, dummy):
        self.dummy = dummy

    #To be discussed
    def get_press(self, data):
        self.pressure = data

class Cable():
    def _init_(self, dummy):
        self.dummy = dummy

    def tighten(self, force):
        pass

    def relax(self, force):
        pass

class Tentacle():
    def __init__(self, n_phalanx: int):
        self.phalanx = []
        for _ in range(n_phalanx):
            self.phalanx.append(Phalanx())
        self.cable_1 = Cable(0)
        self.cable_2 = Cable(1)
        self.cable_3 = Cable(2)

    # Just a dummy function prototype
    def twist_1(self):
        self.cable_1.tighten(3)
        self.cable_2.relax(2)
        self.cable_3.relax(3)

