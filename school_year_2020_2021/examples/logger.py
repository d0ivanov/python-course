class Logger:
    LEVELS = {
            'DEBUG': 0,
            'INFO': 1,
            'WARNING': 2,
            'ERROR': 3,
            }

    def __init__(self, level):
        self._level = self.LEVELS[level]

    def info(self, msg):
        if self.LEVELS['INFO'] >= self._level:
            self._log(msg)

    def error(self, msg):
        if self.LEVELS['ERROR'] >= self._level:
            self._log(msg)

    def debug(self, msg):
        if self.LEVELS['DEBUG'] >= self._level:
            self._log(msg)

    def warning(self, msg):
        if self.LEVELS['WARNING'] >= self._level:
            self._log(msg)

    def _log(self, msg):
        raise NotImplementedError("log(msg) not implemented in " + self)

class StdOutLogger(Logger):
    def _log(self, msg):
        print(msg)

class FileLogger(Logger):
    def __init__(self, level, filename):
        super().__init__(level)
        self.__file = open(filename, 'a')

    def _log(self, msg):
        self.__file.write(msg + '\n')

    def __del__(self):
        self.__file.close()


stdlog = StdOutLogger('ERROR')
stdlog.info("test")
stdlog.error("test 2")

flog = FileLogger('INFO', "dev.log")
flog.info("file test log")
flog.error("file test log 2")
