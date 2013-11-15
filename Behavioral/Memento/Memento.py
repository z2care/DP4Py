'''
Created on 2013-11-15

@author: zhangzhi
@contact: z2care@gmail.com
'''

class Originator:
    def __init__(self):
        self.state = ""
    def createMemento(self):
        return Memento(self.state)
    def setMemento(self, memento):
        self.state = memento.state
    def show(self):
        print("Current state: "+self.state)

class Memento:
    def __init__(self, state):
        self._state = state
    @property
    def state(self):
        return self._state

class CareTaker:
    @property
    def savedMemento(self):
        return self._savedMemento
    @savedMemento.setter
    def savedMemento(self, memento):
        self._savedMemento = memento

if __name__ == "__main__":
    originator = Originator()
    originator.state = "On"
    originator.show()
     
    careTaker = CareTaker()
    careTaker.savedMemento = originator.createMemento()
     
    originator.state = "Off"
    originator.show()
     
    originator.setMemento(careTaker.savedMemento)
    originator.show()
