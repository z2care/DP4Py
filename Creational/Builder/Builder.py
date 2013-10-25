'''
Created on 2013-10-21

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import abstractmethod
from datetime import datetime

class Message(object):
    def __init__(self, type_name):
        self.type = type_name
        self.limit = None
        self.text = None
        self.time = None

    def send(self):
        print "this is a " + self.type + "Message with text " + self.text + " at " + str(self.time) 

class Builder(object):
    @abstractmethod
    def setLimit(self):
        raise    
    @abstractmethod
    def inputText(self):
        raise
    @abstractmethod
    def buildTime(self):
        raise

class SMSBuilder(Builder):
    def __init__(self):
        self.MSG = Message("SMS")
    def setLimit(self):
        self.MSG.limit = 70
    def inputText(self):
        self.MSG.text = "please input your short message"
    def buildTime(self):
        self.MSG.time = datetime.now()

class MailBuilder(Builder):
    def __init__(self):
        self.MSG = Message("Mail")
    def setLimit(self):
        self.MSG.limit = 1024
    def inputText(self):
        self.MSG.text = "please input your long message"
    def buildTime(self):
        self.MSG.time = datetime.now()

class Director(object):
    def __init__(self):
        self.builder = None
    def create(self):
        assert not self.builder is None, "No defined builder"
        self.builder.setLimit()
        self.builder.inputText()
        self.builder.buildTime()
        return self.builder.MSG

if __name__ == '__main__':
    
    director = Director()
    director.builder = SMSBuilder()
    mymsg = director.create()
    mymsg.send()
    