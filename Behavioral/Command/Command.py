'''
Created on 2013-11-15

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Command():
    __metaclass__ = ABCMeta
    @abstractmethod
    def execute(self):
        raise NotImplemented()

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.action()

class Receiver(object):
    def __init__(self, var):
        self._var = var
    def action(self):
        print self._var + ' execute the command.'

class Invoker(object):
    def __init__(self, command):
        self._command = command;
    def action(self):
        self._command.execute()

if __name__ == "__main__":
    receiver = Receiver('Tom')
    
    command = ConcreteCommand(receiver)
    
    invoker = Invoker(command)
    invoker.action()
