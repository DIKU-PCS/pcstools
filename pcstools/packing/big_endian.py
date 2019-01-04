# -*- coding: utf-8 -*-

__all__ = ['pack8', 'pack16', 'pack32', 'pack64',
           'unpack8', 'unpack16', 'unpack32', 'unpack64']

import pcstools.packing
import struct
from pcstools.compat import is_bytes


def pack8(arg):
    r"""Packs a thing into a bytestring, while recursively decending into iterables.

    Integers are packed as 8-bit, unsigned, big-endian values.

    Byte-strings are packed as-is.

    Unicode-strings are utf-8 encoded.

    Examples:
        >>> from pcstools.packing.big_endian import pack8
        >>> pack8(0x41)
        b'A'
        >>> pack8([0x41, 0x42])
        b'AB'
        >>> pack8([0x41, 0x42, ["hello"]])
        b'ABhello'
        >>> pack8(u'☃')
        b'\xe2\x98\x83'
        >>> pack8(-1)
        Traceback (most recent call last):
           ...
        AssertionError: Number must be positive and below 2**8, but number == -1
    """

    return pcstools.packing.pack('>B', 8, arg)


def pack16(arg):
    r"""Packs a thing into a bytestring, while recursively decending into iterables.

    Integers are packed as 16-bit, unsigned, big-endian values.

    Byte-strings are packed as-is.

    Unicode-strings are utf-8 encoded.

    Examples:
        >>> from pcstools.packing.big_endian import pack16
        >>> pack16(0x4241)
        b'BA'
        >>> pack16([0x4241, 0x4142])
        b'BAAB'
        >>> pack16([0x4241, ["hello"]])
        b'BAhello'
        >>> pack16(u'☃')
        b'\xe2\x98\x83'
        >>> pack16(-1)
        Traceback (most recent call last):
           ...
        AssertionError: Number must be positive and below 2**16, but number == -1
    """
    return pcstools.packing.pack('>H', 16, arg)


def pack32(arg):
    r"""Packs a thing into a bytestring, while recursively decending into iterables.

    Integers are packed as 32-bit, unsigned, big-endian values.

    Byte-strings are packed as-is.

    Unicode-strings are utf-8 encoded.

    Examples:
        >>> from pcstools.packing.big_endian import pack32
        >>> pack32(0x44434241)
        b'DCBA'
        >>> pack32([0x44434241, 0x41424344])
        b'DCBAABCD'
        >>> pack32([0x44434241, ["hello"]])
        b'DCBAhello'
        >>> pack32(u'☃')
        b'\xe2\x98\x83'
        >>> pack32(-1)
        Traceback (most recent call last):
           ...
        AssertionError: Number must be positive and below 2**32, but number == -1
    """
    return pcstools.packing.pack('>I', 32, arg)


def pack64(arg):
    r"""Packs a thing into a bytestring, while recursively decending into iterables.

    Integers are packed as 64-bit, unsigned, big-endian values.

    Byte-strings are packed as-is.

    Unicode-strings are utf-8 encoded.

    Examples:
        >>> from pcstools.packing.big_endian import pack64
        >>> pack64(0x4847464544434241)
        b'HGFEDCBA'
        >>> pack64([0x4847464544434241, 0x4142434445464748])
        b'HGFEDCBAABCDEFGH'
        >>> pack64([0x4847464544434241, ["hello"]])
        b'HGFEDCBAhello'
        >>> pack64(u'☃')
        b'\xe2\x98\x83'
        >>> pack64(-1)
        Traceback (most recent call last):
           ...
        AssertionError: Number must be positive and below 2**64, but number == -1
    """
    return pcstools.packing.pack('>Q', 64, arg)


def unpack8(s):
    r"""Unpacks a bytestring into an integer.

    The integer is unpacked as a 8-bit, unsigned, big-endian values.

    Examples:
        >>> from pcstools.packing.big_endian import unpack8
        >>> unpack8(b'A')
        65
        >>> unpack8(b'\x01')
        1
        >>> unpack8(b'')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be of length 1
        >>> unpack8(u'A')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be a bytestring
    """
    assert is_bytes(s), "Argument must be a bytestring"
    assert len(s) == 1, "Argument must be of length 1"
    return struct.unpack('>B', s)[0]


def unpack16(s):
    r"""Unpacks a bytestring into an integer.

    The integer is unpacked as a 16-bit, unsigned, big-endian values.

    Examples:
        >>> from pcstools.packing.big_endian import unpack16
        >>> unpack16(b'AB')
        16706
        >>> unpack16(b'\x01\x00')
        256
        >>> unpack16(b'\x00\x01')
        1
        >>> unpack16(b'')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be of length 2
        >>> unpack16(u'AB')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be a bytestring
    """

    assert is_bytes(s), "Argument must be a bytestring"
    assert len(s) == 2, "Argument must be of length 2"
    return struct.unpack('>H', s)[0]


def unpack32(s):
    r"""Unpacks a bytestring into an integer.

    The integer is unpacked as a 32-bit, unsigned, big-endian values.

    Examples:
        >>> from pcstools.packing.big_endian import unpack32
        >>> unpack32(b'ABCD')
        1094861636
        >>> unpack32(b'\x01\x00\x00\x00')
        16777216
        >>> unpack32(b'\x00\x00\x00\x01')
        1
        >>> unpack32(b'')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be of length 4
        >>> unpack32(u'ABCD')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be a bytestring
    """

    assert is_bytes(s), "Argument must be a bytestring"
    assert len(s) == 4, "Argument must be of length 4"
    return struct.unpack('>I', s)[0]


def unpack64(s):
    r"""Unpacks a bytestring into an integer.

    The integer is unpacked as a 64-bit, unsigned, big-endian values.

    Examples:
        >>> from pcstools.packing.big_endian import unpack64
        >>> unpack64(b'ABCDEFGH')
        4702394921427289928
        >>> unpack64(b'\x01\x00\x00\x00\x00\x00\x00\x00')
        72057594037927936
        >>> unpack64(b'\x00\x00\x00\x00\x00\x00\x00\x01')
        1
        >>> unpack64(b'')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be of length 8
        >>> unpack64(u'ABCDEFGH')
        Traceback (most recent call last):
           ...
        AssertionError: Argument must be a bytestring
    """

    assert is_bytes(s), "Argument must be a bytestring"
    assert len(s) == 8, "Argument must be of length 8"
    return struct.unpack('>Q', s)[0]
