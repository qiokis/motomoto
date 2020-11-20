from abc import ABC, abstractmethod


class LanguageDeterminant:

    def create_compiler(self, language):
        if language == "Java":
            return self._create_java_compiler()
        elif language == "Python":
            return self._create_python_compiler()
        elif language == "C":
            return self._create_c_compiler()
        else:
            return self._return_error()

    def _create_java_compiler(self):
        return JavaCompiler()

    def _create_python_compiler(self):
        return PythonCompiler()

    def _create_c_compiler(self):
        return CCompiler()

    def _return_error(self):
        raise Exception("Such language don't support")


class Compiler(ABC):

    code = None

    def load_code(self, code):
        self.code = code

    def compile(self):
        if self.code:
            print(self.build_lexeme_table())
            print(self.build_identifier_table())
            print(self.build_dsr())
            print(self.build_triad())
            print(self.optimize())
            print(self.build_object_code())

    @abstractmethod
    def build_lexeme_table(self):
        """Реализация построения таблицы лексем"""

    @abstractmethod
    def build_identifier_table(self):
        """Реализация построения таблицы идентификаторов"""

    @abstractmethod
    def build_dsr(self):
        """Реализация построения DSR"""

    @abstractmethod
    def build_triad(self):
        """Реализация построения триады"""

    @abstractmethod
    def optimize(self):
        """Реализация оптимизации"""

    @abstractmethod
    def build_object_code(self):
        """Реализация получения обхектного кода"""


class JavaCompiler(Compiler):

    def build_lexeme_table(self):
        """Реализация построения таблицы лексем"""

    def build_identifier_table(self):
        """Реализация построения таблицы идентификаторов"""

    def build_dsr(self):
        """Реализация построения DSR"""

    def build_triad(self):
        """Реализация построения триады"""

    def optimize(self):
        """Реализация оптимизации"""

    def build_object_code(self):
        """Реализация получения обхектного кода"""


class PythonCompiler(Compiler):

    def build_lexeme_table(self):
        """Реализация построения таблицы лексем"""

    def build_identifier_table(self):
        """Реализация построения таблицы идентификаторов"""

    def build_dsr(self):
        """Реализация построения DSR"""

    def build_triad(self):
        """Реализация построения триады"""

    def optimize(self):
        """Реализация оптимизации"""

    def build_object_code(self):
        """Реализация получения обхектного кода"""


class CCompiler(Compiler):

    def build_lexeme_table(self):
        """Реализация построения таблицы лексем"""

    def build_identifier_table(self):
        """Реализация построения таблицы идентификаторов"""

    def build_dsr(self):
        """Реализация построения DSR"""

    def build_triad(self):
        """Реализация построения триады"""

    def optimize(self):
        """Реализация оптимизации"""

    def build_object_code(self):
        """Реализация получения обхектного кода"""


class DialogManager:

    determinant = LanguageDeterminant()
    comp = None

    def start_dialog(self):
        print("1. Смена / задание языка\n"
              "2. Ввести код\n"
              "3. Построить таблицу лексем\n"
              "4. Построить таблицу идентификаторов\n"
              "5. Построить ДСР\n"
              "6. Построить триады\n"
              "7. Вывести результат оптимизации\n"
              "8. Вывести объектный код\n"
              "9. Произвести все операции\n"
              "0. Выход")
        while (answer := input("Ваш ответ: ")) != "0":
            if answer == "1":
                self.comp = self.determinant.create_compiler(input("Введите язык программирования: ").title())
            elif answer == "2":
                self.comp.load_code(input("Введите код: "))
            elif answer == "3":
                self.comp.build_lexeme_table()
            elif answer == "4":
                self.comp.build_identifier_table()
            elif answer == "5":
                self.comp.build_dsr()
            elif answer == "6":
                self.comp.build_triad()
            elif answer == "7":
                self.comp.optimize()
            elif answer == "8":
                self.comp.build_object_code()
            elif answer == "9":
                self.comp.compile()


if __name__ == "__main__":
    manager = DialogManager()
    manager.start_dialog()
