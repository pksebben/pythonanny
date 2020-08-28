import os
import unittest
import nanny


def setUpModule():
    pass


class TestNanny(unittest.TestCase):

    """the next two are run in order, the third at the end of testing"""
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_logs_created(self):
        self.assertTrue(os.path.exists("pythonanny.log"))

    def _fail(self):
        y = 5 / 0

    def test_fail(self):
        self._fail()

    def _run_failure_code(self):
        try:
            self._fail()
        except Exception as e:
            nanny.nanny_log(e)

    def test_error_logged(self):
        # TODO: check if the logs have been addded to
        self._run_failure_code()
        self.assertTrue()


if __name__ == "__main__":
    unittest.main()
