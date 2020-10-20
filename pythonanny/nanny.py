import json
import traceback
import uuid
import datetime
import sys
import os

logfile = 'nanny.log' 
logdir = os.path.expanduser('~/Documents/')
logpath = logdir + logfile

class Structured_Error:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % json.dumps(self.kwargs)


def nanny_log(type_, val, tb):

    with open(logpath, "a") as f:
        print(
            Structured_Error(
                id='%s' % uuid.uuid4(),
                stack_trace=traceback.format_tb(tb),
                error_type=str(type_),
                # TODO: strip everything but the name of the type
                timestamp=str(datetime.datetime.now())
            ), file=f)


# TODO: May want to remove the print_exception, depending on
# how this behaves with the compound exception hook impl
def nanny_exception_hook(type_, val, tb):
    print("python nanny is saving your exceptions to " + logpath)
    nanny_log(type_, val, tb)

