'''
Created on 2013-11-15

@author: zhangzhi
@contact: z2care@gmail.com
'''

class Handler():
    def successor(self, successor):
        self._successor = successor


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request > 0 and request <= 10:
            print("handle by level A")
        else:
            self._successor.handle(request) 

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request > 10 and request <= 20:
            print("handle by level B")
        else:
            self._successor.handle(request)

class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request > 20 and request <= 30:
            print("handle by level C")
        else:
            print('{} is out of range'.format(request))

if __name__ == "__main__":
    handlerA = ConcreteHandlerA()
    handlerB = ConcreteHandlerB()
    handlerC = ConcreteHandlerC()

    handlerA.successor(handlerB)
    handlerB.successor(handlerC)

    scores = [5,15,25,35]
    for score in scores:
        handlerA.handle(score)
