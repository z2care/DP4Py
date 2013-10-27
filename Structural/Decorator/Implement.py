'''
Created on 2013-10-25

@author: zhangzhi
@contact: z2care@gmail.com
'''
import time

def calcTime(func):
    def decorator(*args,**kwargs):
        before = time.time()
        runIt = func(*args,**kwargs)
        after = time.time()
        print 'total excution time=', after-before, 'seconds'
        return runIt
    return decorator

@calcTime
def someActons():
    time.sleep(1)

if __name__ == "__main__":
    someActons()