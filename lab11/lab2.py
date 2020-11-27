from abc import ABC, abstractmethod, abstractproperty


class Compiler(ABC):

    name: str
    code: str

    def set_code(self, code):
        self.code = code

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

    def compile(self):
        self.build_lexeme_table()
        self.build_identifier_table()
        self.build_dsr()
        self.build_triad()
        self.optimize()
        self.build_object_code()


class PythonCompiler(Compiler):

    code: str
    name = "PythonCompiler"

    def build_lexeme_table(self):
        print(f"I'm {self.name}, I've done lexeme table")

    def build_identifier_table(self):
        print(f"I'm {self.name}, I've done identifier table")

    def build_dsr(self):
        print(f"I'm {self.name}, I've done dsr")

    def build_triad(self):
        print(f"I'm {self.name}, I've done triad table")

    def optimize(self):
        print(f"I'm {self.name}, I've done optimization")

    def build_object_code(self):
        print(f"I'm {self.name}, I've done object code")


class JavaCompiler(Compiler):

    name = "JavaCompiler"
    code: str

    def build_lexeme_table(self):
        print(f"I'm {self.name}, I've done lexeme table")

    def build_identifier_table(self):
        print(f"I'm {self.name}, I've done identifier table")

    def build_dsr(self):
        print(f"I'm {self.name}, I've done dsr")

    def build_triad(self):
        print(f"I'm {self.name}, I've done triad table")

    def optimize(self):
        print(f"I'm {self.name}, I've done optimization")

    def build_object_code(self):
        print(f"I'm {self.name}, I've done object code")


class CCompiler(Compiler):

    name = "CCompiler"
    code: str

    def build_lexeme_table(self):
        print(f"I'm {self.name}, I've done lexeme table")

    def build_identifier_table(self):
        print(f"I'm {self.name}, I've done identifier table")

    def build_dsr(self):
        print(f"I'm {self.name}, I've done dsr")

    def build_triad(self):
        print(f"I'm {self.name}, I've done triad table")

    def optimize(self):
        print(f"I'm {self.name}, I've done optimization")

    def build_object_code(self):
        print(f"I'm {self.name}, I've done object code")


class Moderator:

    lang_name: str = None
    compiler: Compiler = None

    def set_lang(self, lang_name):
        self.lang_name = lang_name

    def create_compiler(self):
        if self.lang_name.lower() == "python":
            self.compiler = PythonCompiler()
            self.compiler.set_code("Введите код: ")
        if self.lang_name.lower() == "java":
            self.compiler = JavaCompiler()
            self.compiler.set_code("Введите код: ")
        if self.lang_name.lower() == "c":
            self.compiler = CCompiler()
            self.compiler.set_code("Введите код: ")

    def compile(self, file_path):
        self.compiler.compile()


if __name__ == "__main__":
    moder = Moderator()
    moder.set_lang(input("Введите язык: "))
    moder.create_compiler()
    moder.compile("path_to_code.language_expansion")
