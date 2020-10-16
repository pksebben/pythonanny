import json
import traceback
import uuid
import datetime
import sys
import subprocess
import argparse
import pdb

# Dump error data 
class Structured_Error:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % json.dumps(self.kwargs)

# Write error data
def nanny_log(type_, val, tb):

    with open("nanny.log", "a") as f:
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

# init() is broken up to allow for both methods of implementation:
# method 1 : run two python scripts together (which would call init in __main__)
# method 2 : import this module, and run init() explicitly

# TODO: Now that we're using packaging in a sane manner, this subproc hackaround can go.
def init():
    sys.excepthook = nanny_exception_hook
    parser = argparse.ArgumentParser(
        description="run a file wrapped in pythonanny's error logger")
    parser.add_argument('filename')
    args = parser.parse_args()
    subprocess.run(["python3", args.filename])


if __name__ == "__main__":
    init()
