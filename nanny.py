import json
import traceback
import uuid
import datetime


class Structured_Error:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % json.dumps(self.kwargs)


def nanny_log(error):

    with open("nanny.log", "a") as f:
        print(
            Structured_Error(
                id='%s' % uuid.uuid4(),
                stack_trace=traceback.format_exc(),
                error_type=str(type(error)),
                # TODO: strip everything but the name of the type
                timestamp=str(datetime.datetime.now())
            ), file=f)
