import sys


class Numbers(object):
    # Конструктор класса
    def __init__(self, *args):
        self.nums = []
        for i in args[0]:
            self.nums.append(i)

    # Функция суммирования
    def sum(self):
        return sum(self.nums)


# Обработка аргументов командной строки
inp = []
for i in sys.argv[1:]:
    inp.append(int(i))

# Создание объекта класса Numbers
r1 = Numbers(inp)
# Вывод результата
print(r1.sum())
