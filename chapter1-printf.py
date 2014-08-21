#!/usr/bin/env python

from ctypes import *

#libc = CDLL("libc.so.6")
libc = CDLL("libSystem.dylib")
libdtrace = CDLL("libdtrace.dylib")
print libdtrace
message_string = "Hello, world!\n"
print dir(libc)
libc.printf("Testing: %s", message_string)
