#!/usr/bin/env python

from ctypes import *

class barley_amount(Union):
    _fields_ = [
            ('barley_long', c_long),
            ('barley_int', c_int),
            # multiply by 8 for an 8 item char array
            ('barley_char', c_char * 8),
            ]

value = raw_input("Enter the amount of barley:")
my_barley = barley_amount(int(value))
print "Barley amount as long: %ld" % my_barley.barley_long
print "Barley amount as int: %d" % my_barley.barley_int
print "Barley amount as char: %s" % my_barley.barley_char
