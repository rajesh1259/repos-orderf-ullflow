from dicti import calculator


class chilcal(calculator):
    num2=50

    def __init__(self):
        calculator.__init__(self,4,8)

    def childmethod(self):
        return self.firstmethod() + self.num + self.num2


obj2=chilcal()
print(obj2.firstmethod())
