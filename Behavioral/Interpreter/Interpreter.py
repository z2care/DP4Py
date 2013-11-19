'''
Created on 2013-11-19

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class AbstractExpression():
    __metaclass__ = ABCMeta
    @abstractmethod
    def interpret(self, context):
        raise NotImplementedError()

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        print "Terminal Interpret"

class NormalExpression(AbstractExpression):
    def interpret(self, context):
        print "Normal Interpret"

class Context(object):
    def __init__(self, arg_string):
        self.arg_string = arg_string

if __name__ == '__main__':
    c = Context("context text")
    sentence = []
    sentence.append(NormalExpression())
    sentence.append(TerminalExpression())
    sentence.append(NormalExpression())

    for expression in sentence:
        expression.interpret(c)
