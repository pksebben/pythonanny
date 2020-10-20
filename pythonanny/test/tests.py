import os
import unittest
import nanny
from subprocess import Popen, PIPE
import sys
import time


def setUpModule():
    # #nanny.init()
    pass

class TestNanny(unittest.TestCase):

    """the next two are run in order, the third at the end of testing"""
    @classmethod
    def setUpClass(cls):
        cls.logfile = nanny.logfile
        pass

    def setUp(self):
        #nanny.init()
        pass

    def tearDown(self):
        pass

    def test_logs_created(self):
        self.assertTrue(os.path.exists(self.logfile))

    # this, for some reason, borked the actual logging.  Keeping it here for forensics later.
    # see devlog LOG_TAG #0001
    # def _run_failure_code_new(self):
    #     proc = Popen([sys.executable, "failtest.py"], stdout=PIPE, stderr=PIPE)
    #     proc.terminate()
    #     proc.kill()
    #     # stdout, stderr = proc.communicate()
    #     # assert proc.returncode == 1
        

    def test_error_logged(self):
        begin_log_size = os.stat(self.logfile).st_size
        # self._run_failure_code_new()
        proc = Popen([sys.executable, "failtest.py"], stdout=PIPE, stderr=PIPE)
        time.sleep(1)
        end_log_size = os.stat(self.logfile).st_size
        print("end log size = " + str(end_log_size) + "\nbegin log size = " + str(begin_log_size))
        # TODO: despite terminate() and kill() I'm still spitting complaints about orphaned processes. 
        proc.terminate()
        proc.kill()
        self.assertTrue(end_log_size > begin_log_size)


if __name__ == "__main__":
    unittest.main()
