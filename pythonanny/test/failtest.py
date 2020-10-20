"""
This test is necessary because when overriding sys.excepthook, the effects don't become visible until the error has propagated through the entire stack - at which point testing becomes difficult.  Thus, we run this in a subprocess and look at the results.
"""

import nanny

# nanny.init()


class NannyTestError(Exception):
    pass


raise NannyTestError
