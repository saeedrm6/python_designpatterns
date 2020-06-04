class SingletonObject(object):
    instance = None

    class __SingletoneObject():
        def __init__(self):
            self.val = None

        def __str__(self):
            return '{0!r} {1}'.format(self, self.val)

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletoneObject()
        return SingletonObject.instance