class Calculator(object):

    def __init__(self):
        self._current_result = 0

    def add(self, a, b=None):
        if b:
            self._current_result = self.__add(a, b)
        else:
            self._current_result = self.__add(a, self._current_result)
        return self._current_result

    def subtract(self, a, b=None):
        if b:
            self._current_result = self.__subtract(a, b)
        else:
            self._current_result = self.__subtract(self._current_result, a)
        return self._current_result

    def multiply(self, a, b=None):
        if b:
            self._current_result = self.__multiply(a, b)
        else:
            self._current_result = self.__multiply(a, self._current_result)
        return self._current_result

    def divide(self, a, b=None):
        if b:
            self._current_result = self.__divide(a, b)
        else:
            self._current_result = self.__divide(self._current_result, a)
        return self._current_result

    def clear(self):
        self._current_result = 0

    def __add(self, a, b):
        return a + b

    def __subtract(self, a, b):
        return a - b

    def __multiply(self, a, b):
        return a * b

    def __divide(self, a, b):
        return a / b
