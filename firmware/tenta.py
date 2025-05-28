class Cable():
    def _init_(self, id):
        self.dummy = id

    def tighten(self, force):
        pass

    def relax(self, force):
        pass

class Tentacle():
    def __init__(self, n_phalanx: int):
        self.cable_1 = Cable(1)
        self.cable_2 = Cable(2)
        self.cable_3 = Cable(3)

    # Just a dummy function prototype
    def twist_1(self):
        self.cable_1.tighten(3)
        self.cable_2.relax(2)
        self.cable_3.relax(3)



### Observaciones movimiento: mod 3d(!) cable.length 35 cm