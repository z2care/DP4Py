'''
Created on 2013-10-24

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Target():
    __metaclass__ = ABCMeta
    @abstractmethod
    def request(self): pass

class Client(Target):
    def request(self):
        print('Client')

class Adaptee:
    def specificRequest(self):
        print('Adaptee')
 
class Adapter(Target):
    adaptee = None
    def request(self):
        return self.adaptee.specificRequest()

if __name__ == '__main__':
    new_client = Adapter()
    new_client.adaptee = Adaptee()
    new_client.request()
    