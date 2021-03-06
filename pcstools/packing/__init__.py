from __future__ import unicode_literals, print_function, absolute_import, division
import struct
from pcstools.compat import is_int, is_bytes, is_unicode, is_iterable, is_bytearray

__all__ = [u'big_endian', u'little_endian']


def pack(format, bits, arg):
    if is_int(arg):
        if 0 <= arg < 2**bits:
            return struct.pack(format, arg)
        else:
            raise ValueError("Number must be positive and below 2**{}, but number == {}".format(
                bits, arg))
    elif is_bytes(arg):
        return arg
    elif is_unicode(arg):
        return arg.encode('utf-8')
    elif is_bytearray(arg):
        return bytes(arg)
    elif is_iterable(arg):
        return b''.join(pack(format, bits, a) for a in arg)
    else:
        raise ValueError(u"Cannot pack value {}".format(arg))
