import os
import glob
import datetime as dt

class Logging:

    def __init__(self,name):
        self.name = name
        cwd = os.getcwd()+'\\'
        self.loggingFile = cwd+'{0}.log'.format(name)
        mode = 'a' if os.path.exists(self.loggingFile) else 'w'
        try:
            with open(self.loggingFile, mode): pass
        except : print('bla')

        
    def log(self,_messegeType,_loggingMessege):
        logMsg = str(dt.datetime.now().strftime("%d-%m-%Y %H:%M")) +' '+_messegeType+': '+_loggingMessege + '\n' 
        with open(self.loggingFile,'a') as f:
            f.write(logMsg)