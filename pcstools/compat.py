import sys
import collections

if sys.version_info < (3,):
    integer_types = (int, long,)
    bytes_type = bytes  # "bytes" == "str" == a slice of bytes
    unicode_type = unicode  # "unicode" == a valid unicode string
    iterable_type = collections.Iterable
else:
    integer_types = (int,)
    bytes_type = bytes  # "bytes" == a slice of bytes
    unicode_type = str  # "str" == a valid unicode string, "unicode" is undefined
    iterable_type = collections.abc.Iterable


def is_int(n):
    return isinstance(n, integer_types)


def is_bytes(s):
    return isinstance(s, bytes_type)


def is_unicode(s):
    return isinstance(s, unicode_type)


def is_iterable(s):
    return isinstance(s, iterable_type)
