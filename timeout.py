from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    print "SUCCESS>?"
    def decorator(func):
        def _handle_timeout(signum, frame):
            print "TIMEOUT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>?"
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            print "WRAPPER>?"
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator
