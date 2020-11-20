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

    @abstractmethod
    def compile(self, code):
        pass


class JavaCompiler(Compiler):

    def compile(self, code):
        """Реализация компиляции"""


class PythonCompiler(Compiler):

    def compile(self, code):
        """Реализация компиляции"""


class CCompiler(Compiler):

    def compile(self, code):
        """Реализация компиляции"""


if __name__ == "__main__":
    determinant = LanguageDeterminant()
    comp = determinant.create_compiler("Python")
    comp.compile("code.txt")




