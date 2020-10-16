"""
this is a test to ensure that importing nanny.py successfully implements sys.excepthook
"""

import nanny

# nanny.init()


class NannyTestError(Exception):
    pass


raise NannyTestError
