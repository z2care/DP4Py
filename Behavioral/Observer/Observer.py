'''
Created on 2013-11-7

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Observer():
    __metaclass__ = ABCMeta
    @abstractmethod
    def update(self):
        raise NotImplementedError()

class ConcreteObserverA(Observer):
    def update(self, event):
        print "observerA received event:%s"%(event)

class ConcreteObserverB(Observer):
    def update(self, event):
        print "observerB received event:%s"%(event)

class Subject():
    __metaclass__ = ABCMeta
    @abstractmethod
    def registerObserver(self, observer):
        raise NotImplementedError()
    @abstractmethod
    def unregisterObserver(self, observer):
        raise NotImplementedError()
    @abstractmethod
    def notifyObserver(self):
        raise NotImplementedError()

class ConcreteSubject(Subject):
    observerCollection = []
    def registerObserver(self, observer):
        if observer not in self.observerCollection:
            self.observerCollection.append(observer)
    def unregisterObserver(self, observer):
        if observer in self.observerCollection:
            self.observerCollection.remove(observer)
    def notifyObserver(self, event):
        for observer in self.observerCollection:
            observer.update(event)

if __name__ == '__main__':
    coa = ConcreteObserverA()
    cob = ConcreteObserverB()
    
    cs = ConcreteSubject()
    cs.registerObserver(coa)
    cs.registerObserver(cob)
    
    cs.notifyObserver("click event")
    cs.notifyObserver("push event")