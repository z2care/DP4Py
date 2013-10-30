'''
Created on 2013-10-30

@author: zhangzhi
@contact: z2care@gmail.com
'''

from abc import ABCMeta,abstractmethod

class Driver():
    ___metaclass__ = ABCMeta    
    @abstractmethod
    def queryDBName(self):
        raise NotImplementedError()

class OracleDriver(Driver):
    def queryDBName(self):
        return "Oracle Support."

class DB2Driver(Driver):
    def queryDBName(self):
        return "DB2 Support."

class DriverManager():
    def __init__(self,driver):
        self.driver = driver    
    def connect(self):
        pass

class WindowsDriverManager(DriverManager):
    def connect(self):
        print "Windows have " + self.driver.queryDBName()

class LinuxDriverManager(DriverManager):
    def connect(self):
        print "Linux have " + self.driver.queryDBName()

if __name__ == '__main__':
    oracle = OracleDriver()
    db2 = DB2Driver()
    
    wdm = WindowsDriverManager(oracle)
    wdm.connect()
    wdm = WindowsDriverManager(db2)
    wdm.connect() 
    
    ldm = LinuxDriverManager(oracle)
    ldm.connect()
    ldm = LinuxDriverManager(db2)
    ldm.connect()
