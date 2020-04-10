class Element:
    def __init__(self, T_hardening, T_vapor, Temp_cur, scale):
        self.T_hardening = T_hardening
        self.T_vapor = T_vapor
        self.Temp_cur = Temp_cur
        self.scale = scale

    def _Converting_Scale(self):
        if self.scale == "C":
            return self.Temp_cur
        elif self.scale == "K":
            self.Temp_cur = self.Temp_cur + 273
            return self.Temp_cur
        elif self.scale == "F":
            self.Temp_cur = (self.Temp_cur-32)/1.8
            return self.Temp_cur

class State(Element):

    def agg_state(self):
        if self.scale == "C":
            pass
        else:
            self.Temp_cur = self._Converting_Scale()
        if self.Temp_cur < self.T_hardening:
            return ('SOLID')
        elif self.T_hardening <= self.Temp_cur <= self.T_vapor:
            return ('LIQUID')
        elif self.Temp_cur > self.T_vapor:
            return ('STEAM')



if __name__== "__main__":
    Iron = State(1538, 2862, 300, "C")       # SOLID
    print(Iron.agg_state())
    Oxygen = State(-218, -182, -473, "K")    # LIQUID
    print(Oxygen.agg_state())
    Chlorine = State(-100, -34, 86, "F")     # STEAM
    print(Chlorine.agg_state())