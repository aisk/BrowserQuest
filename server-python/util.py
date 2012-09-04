
#def register_callback(name):
#    print locals()
#    def inner_method(method, *args, **kwargs):
#        print locals()
#        def inner2(self, *args, **kwargs):
#            print locals()
#            return method(self, *args, **kwargs)
#        return inner2
#    return lambda method: inner_method(method, name)

class register_callback(object):
    def __init__(self, name):
        self.name = name
        print locals()
    def __call__(method, *args, **kwargs):
        print locals()
        def inner_method(*args, **kwargs):
            print locals()
            return method
        return inner_method
