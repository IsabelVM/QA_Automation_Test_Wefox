import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info= ""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '"+ str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def VerifyListMatch(self, expectedList, actualList):
        """
        Verify two lists matches
        """
        return(set(expectedList)==set(actualList))
