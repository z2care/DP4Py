'''
Created on 2013-10-28

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta,abstractmethod

class Action():
    ___metaclass__ = ABCMeta    
    @abstractmethod
    def takeAction(self):
        raise NotImplementedError()

class LawyerProxy(Action):
    def __init__(self, action):
        self.action = action
    def helpTakeAction(self):
        self.action.takeAction()
        self.action.listEvidences()
        self.action.courtDecision()

class EconomicAction(Action):
    def takeAction(self):        
        print "take action with economic law!"
    def listEvidences(self):
        print "find evidences for the action!"
    def courtDecision(self):
        print "All standup,pronounce judgment!"

if __name__ == '__main__':
    ec = EconomicAction()
    lawyer = LawyerProxy(ec)
    lawyer.helpTakeAction()
    