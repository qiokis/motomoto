import sys
clients = {}


class Users:
    # Конструктор класса
    def __init__(self, name, passw):
        self.name = name
        self.passw = passw
        clients.update({name: passw})

    # Функция аутентификации (сравнение введеного пароля с паролем пользователя)
    def auth(self, passw):
        if clients[self.name] == passw:
            return "Аутентификация успешна"
        else:
            return "Неправильный пароль или логин"


# Обработка аргументов командной строки
inp = []
for i in sys.argv[1:]:
    inp.append(i)

# Создание объекта класса Users
r1 = Users(inp[0], inp[1])
# Вывод результата
print(r1.auth(inp[2]))


