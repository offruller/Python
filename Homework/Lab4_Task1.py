# 1. Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи
# и выведите эти числа.
class GlobalValues:
    L = [0, 0, 1]


class Threebonachi:

    def __init__(self):
        i = 3

        while i < 36:
            GlobalValues.L.append((GlobalValues.L[i - 2] + GlobalValues.L[i - 1] + GlobalValues.L[i - 3]))
            i += 1

    def __iter__(self):
        for i in range(35):
            yield GlobalValues.L[i]

List = Threebonachi()
for number in List:
    print(number)
