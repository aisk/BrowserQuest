import logging

class RegisterCallBackMixin(object):
    def register_callback(self, func_name):
        def func(func):
            logging.debug('register callback %s on %s' %(func.func_name, self))
            setattr(self, func_name, func)
        return func
