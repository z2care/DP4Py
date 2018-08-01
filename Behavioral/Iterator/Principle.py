'''
Created on 2013-11-15

@author: zhangzhi
@contact: z2care@gmail.com
'''
from abc import ABCMeta, abstractmethod

class Iterator():
    __metaclass__ = ABCMeta
    @abstractmethod
    def next(self):
        raise NotImplementedError()

class ListIterator(Iterator):
    items = None
    def __init__(self, items):
        self.items = items

    def next(self):
        if self.items:
            return self.items.pop()
        else:
            raise StopIteration('end of iterator,no element left.')

class Collection():
    __metaclass__ = ABCMeta
    @abstractmethod
    def createIterator(self, items):
        raise NotImplementedError()

class List(Collection):
    items = []
    def insert(self, item):
        self.items.append(item)
    def remove(self, item):
        self.items.remove(item)
    def length(self):
        return len(self.items)
    def createIterator(self):
        return ListIterator(self.items)

if __name__ == '__main__':
    list = List()
    list.insert('tom')
    list.insert('bob')
    list.insert('bill')
    list.insert('jim')
    
    listiterator = list.createIterator()
    for i in range(list.length()):
        print listiterator.next()
