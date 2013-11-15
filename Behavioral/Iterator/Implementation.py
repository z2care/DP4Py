'''
Created on 2013-11-15

@author: zhangzhi
@contact: z2care@gmail.com
'''

# iterator
x = [42, "test", -12.34]
it = iter(x)
try:
    while True:
        x = it.next()
        print x
except StopIteration:
    pass

# generator
def foo(n):
    for i in range(n):
        yield i
 
it = foo(5)
try:
    while True:
        x = it.next()
        print x
except StopIteration:
    pass

#class
class NumberGenerator:
    class Iterator:
        def __init__(self, length):
            self.length = length
            self.number = -1
        def next(self):
            self.number = self.number + 1
            if self.number == self.length:
                raise StopIteration
            return self.number
    def __init__(self, length):
        self.length = length
    def __iter__(self):
        return NumberGenerator.Iterator(self.length)

for n in NumberGenerator(10):
    print(n)