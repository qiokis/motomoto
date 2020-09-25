import mysql.connector
from mysql.connector import Error


# Класс отвечающий за соединение
class Connection(object):

    def __init__(self, address="", db="", user_name="", passw=""):
        self.__address = address
        self.__db = db
        self.__user_name = user_name
        self.__passw = passw
        self.__conn = None

    # Установка соединения
    def establish_connection(self):
        try:
            self.__conn = mysql.connector.connect(host=self.__address,
                                                  database=self.__db,
                                                  user=self.__user_name,
                                                  password=self.__passw)
            if self.__conn.is_connected():
                print("***Connection is successfully established***")
        except Error as e:
            print("Error: {}".format(e))

    # Закрытие соединения
    def close_connection(self):
        self.__conn.close()
        print("***Connection is successfully closed***")

    def get_connection(self):
        return self.__conn


# Класс отвечающий за запросы
class Requests(object):

    def __init__(self, con):
        self.__connection = con

    # Функция выводит список учителей работающих в заданный день в заданной аудитории
    def about_teacher(self, day="", auditory=""):
        curs = self.__connection.cursor()
        curs.execute("Select * from Schedule")
        ids = []
        for i in curs.fetchall():
            if i[curs.column_names.index("Day")] == day and i[curs.column_names.index("Auditorium")] == auditory:
                ids.append(i[curs.column_names.index("Teacher")])
        curs.execute("Select * from Teachers")
        for i in curs.fetchall():
            if i[curs.column_names.index("ID")] in ids:
                print("|Day: {}| Auditory: {}| Teacher: {} {} {}|".format(day, auditory, i[1], i[2], i[3]))

    # Функция выводит список учителей отдыхающих в заданный день
    def chillin(self, day=""):
        curs = self.__connection.cursor()
        curs.execute("Select * from Schedule")
        ids = []
        for i in curs.fetchall():
            if i[curs.column_names.index("Day")] != day:
                ids.append(i[curs.column_names.index("Teacher")])
        curs.execute("Select * from Teachers")
        print("Resting on {}:".format(day))
        for i in curs.fetchall():
            if i[curs.column_names.index("ID")] in ids:
                print("|Surname: {}| Name: {}| Patronymic: {}|".format(i[1], i[2], i[3]))

    # Функция выводит день в который происходит заданное количество занятий
    def count_of_lessons_per_day(self, count=0):
        curs = self.__connection.cursor()
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        curs.execute("Select * from Schedule")
        arr = [x[curs.column_names.index("Day")] for x in curs.fetchall()]
        quantity = [arr.count(x) for x in days]
        for i in range(len(quantity)):
            if quantity[i] == count:
                print("{} lessons on {}".format(count, days[i]))

    # Функция выводит день в котором занято заданное количество аудиторий
    def count_of_auditoriums_per_day(self, count=0):
        curs = self.__connection.cursor()
        curs.execute("Select * from Schedule")
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        auds_on_day = [[] for _ in range(len(days))]
        for i in curs.fetchall():
            if i[curs.column_names.index("Auditorium")] not in \
                    auds_on_day[days.index(i[curs.column_names.index("Day")])]:
                auds_on_day[days.index(i[curs.column_names.index("Day")])].append(
                    i[curs.column_names.index("Auditorium")])
        for i in range(len(auds_on_day)):
            if len(auds_on_day[i]) == count:
                print("{} auditoriums are busy on {}".format(count, days[i]))
                print("Next auditoriums are busy: {}".format(", ".join(auds_on_day[i])))


if __name__ == "__main__":

    connection_obj = Connection("localhost", "kpo", "root")
    connection_obj.establish_connection()
    connection = connection_obj.get_connection()

    request_obj = Requests(connection)

    # request_obj.about_teacher("Monday", "B-150")
    # request_obj.chillin("Friday")
    # request_obj.count_of_lessons_per_day(13)
    # request_obj.count_of_auditoriums_per_day(9)

    connection_obj.close_connection()
