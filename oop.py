# inheritance
class Addmission:
    def __init__(self, name: str, quarter: int, institute="Governer House"):
        self.name = name
        self.quarter = quarter
        self.institute = institute

    def section(self, section: str):
        return section


class Promoted(Addmission):
    def __init__(self, name: str, quarter: int, institute="Governer House"):
        super().__init__(name, quarter, institute)

    def Certified(self, isCertified: bool):
        return f'Also Certified: {isCertified}'


student1 = Addmission("Maryam Faizan", 3)

print(f'{student1.name} is a student in {student1.institute} in Quarter {student1.quarter}')
promoted_student = Promoted("Maryam Faizan", 3)
print(promoted_student.Certified(True))
