from pro010 import Logger

logger1 = Logger()
logger1.filename = "logserver.txt"
logger1.debug("TEST DEBUG NOW")
print(logger1)

logger2 = Logger()
logger2.filename = "logserver.txt"
logger2.debug("TEST DEBUG NOW 2")
print(logger2)