'''
Created on 2013-11-19

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Visitor():
    __metaclass__ = ABCMeta
    @abstractmethod
    def visitConcreteElementA(self):
        raise NotImplemented()
    @abstractmethod
    def visitConcreteElementB(self):
        raise NotImplemented()

class ConcreteVisitor(Visitor):
    def visitConcreteElementA(self, element):
        print ('%s visited by %s' % (element.__class__.__name__, self.__class__.__name__))
    def visitConcreteElementB(self, element):
        print ('%s visited by %s' % (element.__class__.__name__, self.__class__.__name__))

class Element():
    __metaclass__ = ABCMeta
    @abstractmethod
    def accept(self, visitor):
        raise NotImplemented()

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visitConcreteElementA(self)
    def operationA(self):
        pass

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visitConcreteElementB(self)
    def operationB(self):
        pass

class ObjectStructure():
    elements = []
    def attach(self,element):
        self.elements.append(element)
    def detach(self,element):
        self.elements.remove(element)
    def accept(self,visitor):
        for element in self.elements:
            element.accept(visitor)

if __name__ == '__main__':
    client = ObjectStructure()
    client.attach(ConcreteElementA())
    client.attach(ConcreteElementB())

    visitor = ConcreteVisitor()

    client.accept(visitor)
