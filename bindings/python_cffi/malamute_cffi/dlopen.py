################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from __future__ import print_function
import os
import sys
from ctypes.util import find_library

import cffi
ffi = cffi.FFI()

try:
    # If LD_LIBRARY_PATH or your OSs equivalent is set, this is the only way to
    # load the library.  If we use find_library below, we get the wrong result.
    if os.name == 'posix':
        if sys.platform == 'darwin':
            libpath = 'libmlm.1.dylib'
        else:
            libpath = 'libmlm.so.1'
    elif os.name == 'nt':
        libpath = 'libmlm.dll'
    lib = ffi.dlopen(libpath)
except OSError:
    libpath = find_library("malamute")
    if not libpath:
        raise ImportError("Unable to find libmlm")
    lib = ffi.dlopen(libpath)

from malamute_cffi.cdefs import malamute_cdefs

for cdef in malamute_cdefs:
   ffi.cdef (cdef)
