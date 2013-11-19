'''
Created on 2013-11-19

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Mediator():
    __metaclass__ = ABCMeta
    @abstractmethod
    def broadcast(self, message, colleague):
        raise NotImplemented()

class ConcreteMediator(Mediator):
    __colleagueA = None
    __colleagueB = None

    @property
    def colleagueA(self):
        pass
    @colleagueA.setter
    def colleagueA(self, value):
        self.__colleagueA = value

    @property
    def colleagueB(self):
        pass
    @colleagueB.setter
    def colleagueB(self,value):
        self.__colleagueB = value

    def broadcast(self, message, colleague):
        if colleague == self.__colleagueA:
            self.__colleagueB.notify(message)
        else:
            self.__colleagueA.notify(message)

class Colleague():
    def __init__(self,mediator):
        self.mediator = mediator

class ConcreteColleagueA(Colleague):
    def broadcast(self, message):
        self.mediator.broadcast(message, self)
    def notify(self, message):
        print("ColleaugeA obtained message: "+message)

class ConcreteColleagueB(Colleague):
    def broadcast(self, message):
        self.mediator.broadcast(message, self)
    def notify(self, message):
        print("ColleaugeB obtained message: "+message)

if __name__ == '__main__':
    mediator = ConcreteMediator()

    cca = ConcreteColleagueA(mediator)
    ccb = ConcreteColleagueB(mediator)

    mediator.colleagueA = cca
    mediator.colleagueB = ccb

    cca.broadcast('this is cca speaking!')
    ccb.broadcast('this is ccb speaking!')
