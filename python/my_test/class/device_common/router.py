class Router:
    def some(self):
        return self.__class__.__module__+"."+self.__class__.__name__
