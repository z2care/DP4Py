'''
Created on 2013-11-7

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta, abstractmethod

class Duck():
    __metaclass__ = ABCMeta
    @abstractmethod
    def display(self):
        raise NotImplementedError()
    def setFlyBehavior(self, flybehavior):
        self.flyBehavior = flybehavior
    def setQuackBehavior(self, quackbehavior):
        self.quackBehavior = quackbehavior
    def performFly(self):
        self.flyBehavior.fly()
    def performQuack(self):
        self.quackBehavior.quack()

class FlyBehavior():
    __metaclass__ = ABCMeta
    @abstractmethod
    def fly(self):
        raise NotImplementedError()
class FlyWithWings(FlyBehavior):
    def fly(self):
        print "fly with wings!"
class FlyNoWay(FlyBehavior):
    def fly(self):
        print "fly no way!"

class QuackBehavior:
    __metaclass__ = ABCMeta
    @abstractmethod
    def quack(self):
        raise NotImplementedError()
class Quack(QuackBehavior):
    def quack(self):
        print "-ya-ya-"
class Squeak(QuackBehavior):
    def quack(self):
        print "-la-la-"
class MuteQuack(QuackBehavior):
    def quack(self):
        print "--mute--"

class MallardDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Squeak())
    def display(self):
        print "MallardDuck"
class RedheadDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(Quack())
    def display(self):
        print "RedheadDuck"
class RubberDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(MuteQuack())
    def display(self):
        print "RubberDuck"
class DecoyDuck(Duck):
    def __init__(self):
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(MuteQuack())
    def display(self):
        print "DecoyDuck"


if __name__ == "__main__":
    decoy_duck = DecoyDuck()
    decoy_duck.display()
    decoy_duck.performFly()
    decoy_duck.performQuack()
    print#with empty line
    decoy_duck.setFlyBehavior(FlyNoWay())
    decoy_duck.setQuackBehavior(Quack())
    decoy_duck.display()
    decoy_duck.performFly()
    decoy_duck.performQuack()
