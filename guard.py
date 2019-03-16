#coding=utf-8
"""
Create On 2019/3/16

@author: Ron2
"""

import time
import psutil
import commands

PROCESS_NAME_SUFFIX = ""

class Guard(object):
    """
    CentOS守护进程
    """
    def __init__(self, interval = 60):
        """
        :param interval: 
        """
        self.intervalTimeSec = interval
        self.nextCheckTime = 0


    def restartProcess(self):
        """
        重启
        :return: 
        """
        a, b = commands.getstatusoutput('sh /home/Ron/plug_start.sh')
        print a, b


    def checkProcess(self):
        """
        检查进程
        :return: 
        """
        isAlive = False
        allProcessArray = psutil.pids()
        for pid in allProcessArray:
            try:
                pObj = psutil.Process(pid)
                argList = pObj.cmdline()
                argArray = []
                for arg in argList:
                    argArray.append(arg)

                ''' 转成数组后.然后判定参数 '''
                global PROCESS_NAME_SUFFIX
                if argArray[0].endswith(PROCESS_NAME_SUFFIX) == True and argArray[4] == "443":
                    print "find it ==> ", argArray
                    isAlive = True
            except:
                pass


        if isAlive == False:
            self.restartProcess()


    def start(self):
        """
        :return:
         # 每分钟检查
        */1 * * * * /home/Ron/.pyenv/versions/bpsg/bin/python /home/Ron/g.py
        """
        self.checkProcess()
        # while True:
        #     now = time.time()
        #     if now >= self.nextCheckTime:
        #         self.nextCheckTime = now + self.intervalTimeSec
        #         self.checkProcess()
        #
        #     time.sleep(1)








if __name__ == "__main__":
    obj = Guard()
    obj.start()

