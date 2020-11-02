# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class MyClass:
    def __init__(self, palto_1, costum_2):
        self.palto_1 = int(palto_1)
        self.costum_2 = int(costum_2)

    def Palto(self):
        return f"Расчет по формуле для Пальто {(self.palto_1 / 6.5 + 0.5)}"

    def Costum(self):
        return f"Расчет по формуле для Костюма: {2 * self.costum_2 + 0.3}"

    @property
    def my_method(self):
        return f"Общий расход ткани:" \
               f" {round((self.palto_1 / 6.5 + 0.5) + (self.costum_2 * 2 + 0.3))}"


a = MyClass(100, 100)
print(a.Costum())
print(a.Palto())