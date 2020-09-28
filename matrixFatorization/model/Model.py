class Model():

    def __init__(self, name, version):
        self.__name__ = name
        self.__version__ = version

        print("Model initialization")

    def train(self):
        print("Trainning algorithm")

    def predict(self):
        print("Perform some predictions")

    def description(self):
        return "name : {name}, version : {version}".format(name=self.__name__, version=self.__version__)

