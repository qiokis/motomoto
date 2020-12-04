import datetime
import time

import pymysql

holidays = ("12-31", "01-01", "etc.")  # Праздники
host = "localhost"
user = "admin"
password = "admin"
data_base = "skud"
# connection


def connect_to_bd():
    return pymysql.connect(host, user, password, data_base)


def get_bsm_data():
    data = []
    with open("../lab11/bsm_file.txt", "r") as f:
        while (values := f.readline().split("><")) != [""]:
            for i in range(len(values)):
                values[i] = values[i].replace(">", "")
                values[i] = values[i].replace("<", "")
                values[i] = values[i].replace("\n", "")
            data.append(values)
    return data


def insert_to_controller(data):
    """Перебираем дату полученную из СКУД,
     если в таблице есть ключ пришедший из СКУД,
     записываем как время выхода,
    иначе записываем как время входа"""


def insert_to_collector():
    """Берем данные из контроллера и записываем в сборщик,
    определяем отработанное время работника используя начало и конец рабочего дня данного работника,
    а также какой день на момент записи данных (выходной, будничный или праздничный). Удаляем содержимое контроллера"""


def calculate_collector_info():
    """Считаем данные для табеля, расчитывая недороботку
     используя таблицу Работник (норма отработанных часов)"""


def clear_collector():
    """Функция очищает коллектор"""


if __name__ == "__main__":

    connection = connect_to_bd()

    while True:

        info = get_bsm_data()
        insert_to_collector()
        insert_to_controller(info)
        time.sleep(30)
        # Если день месяца первый то используем calculate_collector_info()
        # Если просто хотим то используем calculate_collector_info()

    connection.close()
