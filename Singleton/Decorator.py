'''
Created on 2013-10-19

@author: zarey
'''

def SingletonDecorator(class_):
        
    instances = {}
    def _singleton(*args, **kw):
        if class_ not in instances:  
            instances[class_] = class_(*args, **kw)
        return instances[class_]
    return _singleton

@SingletonDecorator
class Logger(object):
    pass

if __name__ == '__main__':
    a = Logger()
    b = Logger()
    print a
    print b
    assert id(a)==id(b)