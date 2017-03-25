#!/usr/bin/python

import frida
import sys

process = sys.argv[1]

session = frida.attach(int(process))

print("\nModules:\n")
print(session.enumerate_modules())

print("\n##########################\n")

print("\nRanges:\n")
print(session.enumerate_ranges('rw-'))
