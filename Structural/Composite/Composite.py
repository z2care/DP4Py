'''
Created on 2013-10-31

@author: zhangzhi
@contact: z2care@gmail.com
'''
from abc import ABCMeta,abstractmethod

class Composite():
    def __init__(self,name,left,right):
        pass
    ___metaclass__ = ABCMeta    
    @abstractmethod
    def next(self):
        raise NotImplementedError()

class Component(Composite):
    def __init__(self,name,left,right):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return "-"+self.name+"\n"+self.next()
    def next(self):
        return str(self.left)+str(self.right)

class Leaf(Composite):
    def __init__(self,name,left=None,right=None):
        self.name = name
    def __str__(self):
        return "->("+self.name+self.next()
    def next(self):
        return ")\n"

if __name__ == '__main__':
    apple = Leaf("apple")
    orange = Leaf("orange")
    banana = Leaf("banana")
    mango = Leaf("mango")
    subbranch = Component("subbranch", orange, mango)
    branch = Component("branch", apple, subbranch)
    root = Component("root", banana, branch)
    print root
    