'''
Created on 2013-11-18

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class State():
    __metaclass__ = ABCMeta
    @abstractmethod
    def handle(self):
        raise NotImplementedError()

class ConcreteStateA(State):
    '''a class'''
    def __init__(self,context):
        self.context = context
    def handle(self):
        print('%s: -> %s'%(self.context.state.__class__.__name__,self.context.stateB.__class__.__name__))
        self.context.state = self.context.stateB

class ConcreteStateB(State):
    'b class'
    def __init__(self,context):
        self.context = context
    def handle(self):
        print('%s: -> %s'%(self.context.state.__class__.__name__,self.context.stateA.__class__.__name__))
        self.context.state = self.context.stateA

class Context():
    def __init__(self):
        self.stateA = ConcreteStateA(self)
        self.stateB = ConcreteStateB(self)
        self.state = self.stateA
    def request(self):
        self.state.handle()

if __name__ == '__main__':
    context = Context()
    for _ in range(5):
        context.request()
