import logging

class RegisterCallBackMixin(object):
    def register_callback(self, func):
        '''Decorator for auto register'''
        logging.debug('register callback %s on %s' %(func.func_name, self))
        setattr(self, func.func_name, func)
