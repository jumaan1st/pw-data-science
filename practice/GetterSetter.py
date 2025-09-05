class GetterSetter:
    def __init__(self,name):
        self.__name=name

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

