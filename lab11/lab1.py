from abc import ABC, abstractmethod


class Compiler(ABC):

    name: str

    @abstractmethod
    def get_object_code(self):
        """Реализация получения объектного кода"""


class PythonCompiler(Compiler):

    name = "PythonCompiler"

    def get_object_code(self):
        print(f"I'm {self.name}, I've done object code")


class JavaCompiler(Compiler):

    name = "JavaCompiler"

    def get_object_code(self):
        print(f"I'm {self.name}, I've done object code")


class CCompiler(Compiler):

    name = "CCompiler"

    def get_object_code(self):
        print(f"I'm {self.name}, I've done object code")


class Moderator:

    lang_name: str = None
    compiler: Compiler = None

    def set_lang(self, lang_name):
        self.lang_name = lang_name

    def create_compiler(self):
        if self.lang_name.lower() == "python":
            self.compiler = PythonCompiler()
        if self.lang_name.lower() == "java":
            self.compiler = JavaCompiler()
        if self.lang_name.lower() == "c":
            self.compiler = CCompiler()

    def compile(self, file_path):
        self.compiler.get_object_code()


if __name__ == "__main__":
    moder = Moderator()
    moder.set_lang(input("Введите язык: "))
    moder.create_compiler()
    moder.compile("path_to_code.language_expansion")
