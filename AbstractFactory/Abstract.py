'''
Created on 2013-10-17

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

class Provider():
    @abstractmethod
    def produce(self):
        pass

class SendSMSFactory(Provider):
    def produce(self):
        return SMSSender()

class SendMailFactory(Provider):
    def produce(self):
        return MailSender()

if __name__ == "__main__":
    provider = SendSMSFactory()
    sender = provider.produce()
    sender.send()