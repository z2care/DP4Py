'''
Created on 2013-11-4

@author: zhangzhi
@contact: z2care@gmail.com
'''

import weakref

class Printer(object):
    _pool = weakref.WeakValueDictionary()
    
    def __new__(cls, brand):
        obj = Printer._pool.get(brand)
        if not obj:
            obj = object.__new__(cls)
            Printer._pool[brand] = obj
            obj.brand = brand
        return obj

if __name__ == '__main__':
    c1 = Printer('HP')
    c2 = Printer('HP')
    assert c1 is c2
