'''
Created on 2013-10-28

@author: zhangzhi
@contact: z2care@gmail.com
'''

class BIOS():
    def post(self): 
        print "POST routine on..."

class Kernel:
    def excute(self):
        print "Run kernel code..."

class Shell:
    def environment(self):
        print "Initial command line..."

class Computer:
    def __init__(self):
        self.bios = BIOS()
        self.kernel = Kernel()
        self.shell = Shell()

    def boot(self):
        self.bios.post()
        self.kernel.excute()
        self.shell.environment()

if __name__ == '__main__':
    facade = Computer()
    facade.boot()
