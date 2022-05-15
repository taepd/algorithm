class SoccerPlayer(object):
    def __init__(self, name: str):
        self.name = name

abc = SoccerPlayer(4)


class Person:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()

james = Person()
james._Person__greeting()
