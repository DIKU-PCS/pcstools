from pcstools.compat import is_int, is_bytes, is_unicode, is_iterable
import struct
import collections
import pcstools.packing

__all__ = [u'big_endian', u'little_endian']


def pack(format, bits, arg):
    if is_int(arg):
        if not (0 <= arg < 2**bits):
            raise ValueError("Number must be positive and below 2**{}, but number == {}".format(
                bits, arg))
        return struct.pack(format, arg)
    elif is_bytes(arg):
        return arg
    elif is_unicode(arg):
        return arg.encode('utf-8')
    elif is_iterable(arg):
        return b''.join(pack(format, bits, a) for a in arg)
    else:
        raise ValueError(u"Cannot pack value {}".format(arg))
