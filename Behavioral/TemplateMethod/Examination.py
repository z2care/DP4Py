'''
Created on 2013-11-7

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class ExamPaper():
    ___metaclass__ = ABCMeta
    def QuestionA(self):
        print "QuestionA: what's your student number?"
        print self.AnswerA() 
    def QuestionB(self):
        print "QuestionB: please proof is 1+1?"
        print self.AnswerB()
    @abstractmethod
    def AnswerA(self):
        raise NotImplementedError()
    @abstractmethod
    def AnswerB(self):
        raise NotImplementedError()

class StudentTomPaper(ExamPaper):
    def AnswerA(self):
        return "AnswerA: 20131188"
    def AnswerB(self):
        return "AnswerB: sorry, its complicated."

class StudentAlicePaper(ExamPaper):
    def AnswerA(self):
        return "AnswerA: 20131166"
    def AnswerB(self):
        return "AnswerB: its result 2."

if __name__ == '__main__':
    tom = StudentTomPaper()
    tom.QuestionA()
    tom.QuestionB()
    print
    alice = StudentAlicePaper()
    alice.QuestionA()
    alice.QuestionB()