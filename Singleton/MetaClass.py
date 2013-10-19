'''
Created on 2013-10-19

@author: zarey
'''
class SinglMetaclass(type):
    def __init__(self, name, bases, dct):
        super(SinglMetaclass, self).__init__(name, bases, dct)
        self.instance = None

    def __call__(self,*args,**kw):
        if self.instance is None:
            self.instance = super(SinglMetaclass, self).__call__(*args, **kw)
        return self.instance

class Logger(object):
    __metaclass__ = SinglMetaclass

if __name__ == '__main__':
    a = Logger()
    b = Logger()
    print a
    print b
    assert id(a)==id(b)