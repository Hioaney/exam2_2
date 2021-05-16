
class Menanger():
    def __init__(self, name, income, hours, id, *productivity):
        self.name = name
        self.income = income
        self.hours = hours
        self.id = id
        print(f'Имя и Фамилия:"{self.name}". ЗП: {self.income}. Персональный идентификационный номер:"{self.id}"'.format(self.name, self.id))

    def average(self):
        a = 0
        for hours in self.productivity:
            a += hours
        res = a / 40 * 100(self.productivity)
        print(f' Продуктивность Работника {self.name}: {res}%')
        
class Secretary(Menanger):
    def __init__(self, name, income, hours, id, *productivity):
        super().__init__(name, income, hours, id, productivity)

class Seller(Menanger):
    def __init__(self, name, income, sales, id, hours, *productivity):
        super().__init__(name, income, hours, id, productivity)

    def average(self):
        a = 0
        for hours in self.productivity:
            a += hours
        res = a % 40 * 100(self.productivity)
        print(f' Продуктивность Работника {self.name}: {res}%')




menager = Menanger('Барсбек Канаткулов', 45000, 18, 1)
secretary = Menanger('Алымкул Тилекбаев', 20000, 38, 2)
seller = Seller('Айпери Шалымбекова', 20000, 20, 3, 38)

menager.average
secretary.average
seller.average


information = [menager, secretary, seller]

