class Event:
    """
    Reference:
        http://www.valuedlessons.com/2008/04/events-in-python.html
        https://stackoverflow.com/questions/1092531/event-system-in-python

        https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
        https://pythonacademy.com.br/blog/domine-decorators-em-python
        https://wiki.python.org/moin/PythonDecoratorLibrary

        https://pythonacademy.com.br/blog/iterators-e-generators-em-python
    """
    #def _kwargs_str(self):
        #return ", ".join(k+"="+v.__name__ for k, v in self._signature.items())
    def __init__(self):
        self.handlers = set()
    def __iadd__(self, handler):
        self.handlers.add(handler)
        return self
    def __isub__(self, handler):
        try:
            self.handlers.remove(handler)
        except KeyError:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self
    def __call__(self, *args, **kargs):
        for handler in self.handlers:
            handler(*args, **kargs)
    def __len__(self):
        return len(self.handlers)
    def hasHandlers(self):
         return self.__len__() > 0
