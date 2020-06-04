def log_message(msg):
    with open('logserver.txt', 'a') as logfile:
        logfile.write('{0}\n'.format(msg))


def critical(msg):
    with open('logserver.txt', 'a') as logfile:
        logfile.write('[CRITICAL] {0}\n'.format(msg))

def error(msg):
    with open('logserver.txt', 'a') as logfile:
        logfile.write('[ERROR] {0}\n'.format(msg))

def warning(msg):
    with open('logserver.txt', 'a') as logfile:
        logfile.write('[WARNING] {0}\n'.format(msg))

def info(msg):
    with open('logserver.txt', 'a') as logfile:
        logfile.write('[INFO] {0}\n'.format(msg))

def debug(msg):
    with open('logserver.txt', 'a') as logfile:
        logfile.write('[DEBUG] {0}\n'.format(msg))