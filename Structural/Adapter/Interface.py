'''
Created on 2013-10-24

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Target():
    __metaclass__ = ABCMeta
    @abstractmethod
    def requestQuestion(self): pass
    @abstractmethod
    def requestAnswer(self): pass

class Adapter(Target):
    def requestQuestion(self):
        pass
    def requestAnswer(self):
        pass 

class Student(Adapter):
    def requestAnswer(self):
        print('student: i don\'t know...')

class Teacher(Adapter):
    def requestQuestion(self):
        print('teacher: 1+1=?')

if __name__ == '__main__':
    student = Student()
    teacher = Teacher()
    teacher.requestQuestion()
    teacher.requestAnswer()
    student.requestQuestion()
    student.requestAnswer()
