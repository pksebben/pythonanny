import json
import traceback
import uuid
import datetime
import sys
import subprocess
import argparse
import pdb

# TODO: put nanny.log somewhere sane.
# TODO: implement sane checking that nanny.log was created properly.
logfile = "nanny.log"

class Structured_Error:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % json.dumps(self.kwargs)


def nanny_log(type_, val, tb):

    with open(logfile, "a") as f:
        print(
            Structured_Error(
                id='%s' % uuid.uuid4(),
                stack_trace=traceback.format_tb(tb),
                error_type=str(type_),
                # TODO: strip everything but the name of the type
                timestamp=str(datetime.datetime.now())
            ), file=f)


def nanny_exception_hook(type_, val, tb):
    print("python nanny is saving your exceptions")
    traceback.print_exception(type_, val, tb)
    nanny_log(type_, val, tb)
    exit()

sys.excepthook = nanny_exception_hook

if __name__ == "__main__":
    init()
