import datetime

class Singleton:
    _instance = None
 
    def __init__(self):
        raise Exception("Unable to create new instance")
 
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def show_time(self):
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))


class MyClass(Singleton):
    def init(self):
        self.name = "Lee"
        self.age = 10

    def start(self):
        print("NAME:" + self.name)
        print("AGE:" + str(self.age))


my = MyClass.get_instance()
my.init()
my.start()  


