'''
Created on 2013-10-16

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import abstractmethod

class Sender():
    @abstractmethod
    def send(self):
        pass

class SMSSender(Sender):
    def send(self):
        print "I'm SMSSender!"

class MailSender(Sender):
    def send(self):
        print "I'm MailSender!"

class SendFactory():
    def produce(self,types):
        if types == "SMS":
            return SMSSender()
        elif types == "Mail":
            return MailSender()
        else:
            print "error parameter!!!"

if __name__ == "__main__":
    factory = SendFactory()
    sender = factory.produce("SMS")
    sender.send()