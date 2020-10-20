class SimpleArithmetics(object):

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def zero_value(self):
        return 0


class ModularArithmetics(object):

    def __init__(self, modulus):
        self.__modulus = modulus

    def add(self, a, b):
        return (a + b) % self.__modulus

    def subtract(self, a, b):
        return (a - b) % self.__modulus

    def multiply(self, a, b):
        return (a * b) % self.__modulus

    def divide(self, a, b):
        return (a / b) % self.__modulus

    def zero_value(self):
        return 0


class MatrixArithmetics(object):
    pass


class Calculator(object):

    def __init__(self, arithmetics):
        self.__arithmetics = arithmetics
        self._current_result = self.__arithmetics.zero_value()

    def add(self, a, b=None):
        if b:
            self._current_result = self.__arithmetics.add(a, b)
        else:
            self._current_result = self.__arithmetics.add(
                    a, self._current_result)
        return self._current_result

    def subtract(self, a, b=None):
        if b:
            self._current_result = self.__arithmetics.subtract(a, b)
        else:
            self._current_result = self.__arithmetics.subtract(
                    self._current_result, a)
        return self._current_result

    def multiply(self, a, b=None):
        if b:
            self._current_result = self.__arithmetics.multiply(a, b)
        else:
            self._current_result = self.__arithmetics.multiply(
                    a, self._current_result)
        return self._current_result

    def divide(self, a, b=None):
        if b:
            self._current_result = self.__arithmetics.divide(a, b)
        else:
            self._current_result = self.__arithmetics.divide(
                    self._current_result, a)
        return self._current_result

    def clear(self):
        self._current_result = self.__arithmetics.zero_value()

