# pcstools - exploit toolkit for the PCS course
[![Docs](https://readthedocs.org/projects/pcstools/badge/?version=stable)](https://pcstools.readthedocs.io/)
[![PyPI](https://img.shields.io/badge/pypi-v0.4-green.svg?style=flat)](https://pypi.python.org/pypi/pcstools/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

pcstools is an exploit development library heavily inspired by [https://pwntools.com/](pwntools).

It supports both Python 2.7 and Python 3.3+.

# Documentation

Our documentation is available at [pcstools.readthedocs.io](https://pcstools.readthedocs.io/)

# Installation

Pcstools is pure Python library and should be supported on most
platforms. It should even work on non-linux platforms. However
Pcstools is currently being developed exclusively on debian-based
systems, so bugs might be encountered. If this happens, be sure to
file an issue!

To install on debian-based systems, do the following:

```sh
# For usage with Python 2.7
apt update
apt install python-pip
pip2 install --upgrade pcstools

# For usage with Python 3.3+
apt update
apt install python3-pip
pip3 install --upgrade pcstools
```

# How is this project related to pwntools

Pcstools is not directly related to pwntools (though some of the developers
overlap), however the goals of the two projects are very different.

Pwntools tries to be the best possible exploitation library with a particular
focus on CTFs. While it **does** prioritize readability, learnability and doing
things the "normal python way", those values are occationally sacrifized in the
name of productivity (for the exploit developer), performance or advanced
features.

This is not the case for Pcstools. Pcstools tries to be a normal python library
that is **easy to learn** and **easy to understand**. The target user is
someone new to exploitation that just wants to avoid too much boilerplate. We
have deliberately omitted many features, as we believe that they should not be
introduced until the basics have been covered.

# Why the name "Pcstools"?

Pcstools has been developed with a particular target audience in mind: The
students taking the course "Proactive Computer Security" at the Department of
Computer Science at Copenhagen University. 
