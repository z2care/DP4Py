'''
Created on 2013-10-25

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta,abstractmethod

class Component(object):
    ___metaclass__ = ABCMeta    
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print "ConcreteComponent"

class Decorator(Component):
    component = None
    def operation(self):
        self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        super(ConcreteDecoratorA, self).operation()
        self.addedState = True
        print "ConcreteDecoratorA"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        super(ConcreteDecoratorB, self).operation()
        self.addedBehavior()
        print "ConcreteDecorator"
    def addedBehavior(self):
        print "addedBehavior"

if __name__ == "__main__":
    cc = ConcreteComponent()
    cda = ConcreteDecoratorA()
    cdb = ConcreteDecoratorB()
    
    cda.component = cc
    cdb.component = cda
    
    cdb.operation()
    