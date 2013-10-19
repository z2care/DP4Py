'''
Created on 2013-10-19

@author: zarey
'''

class Logger(object):
    
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Logger, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

if __name__ == '__main__':
    a = Logger()
    b = Logger()
    print a
    print b
    assert id(a)==id(b)