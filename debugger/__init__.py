import os
import time
import sys
from libdtrace import LIBDTRACE
from ctype_defs.libdtrace import *


class ProcessStartError(Exception):
    pass


def trace_calls(frame, event, arg):
    with open('./debug.out', 'w+') as f:
        f.write(str(event))

    return


class Debugger():
    def __init__(self):
        self.childpid = None

    def load(self, path):
        if self.start_process(path):
            print "Successfully started", path, "with pid", self.childpid

    def start_process(self, path):
        pid = None
        parent = True
        try:
            pid = os.fork()
        except OSError, e:
            raise ProcessStartError(e.message)

        if pid == 0:
            print "hello from the process being debugged"
            parent = False
            try:
                # get dtrace handle
                handle = LIBDTRACE.dtrace_open(3, 0, byref(c_int(0)))
                 
                # options
                #if LIBDTRACE.dtrace_setopt(handle, "bufsize", "4m") != 0:
                #    txt = LIBDTRACE.dtrace_errmsg(handle, LIBDTRACE.dtrace_errno(handle))
                #    raise Exception(c_char_p(txt).value)

                buf_func = BUFFERED_FUNC(buffered)
                LIBDTRACE.dtrace_handle_buffered(handle, buf_func, None)

                prg = LIBDTRACE.dtrace_program_strcompile(handle, SCRIPT, 3, 4, 0, None)

                # run
                LIBDTRACE.dtrace_program_exec(handle, prg, None)
                LIBDTRACE.dtrace_go(handle)
                LIBDTRACE.dtrace_stop(handle)
                #sys.settrace(trace_calls)
                os.execv(path, ('',))
            except OSError, e:
                raise ProcessStartError(e.message)
        else:
            self.childpid = pid

        return True
