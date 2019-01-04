import glob

from setuptools import find_packages
from setuptools import setup

# Convert README.md to reStructuredText for PyPI
long_description = '''
pcstools - exploit toolkit for the PCS course
=====================================

`MIT License <http://choosealicense.com/licenses/mit/>`__

pcstools is an exploit development library heavily inspired by
`https://pwntools.com/ <pwntools>`__. It is not a design goal to be
API-compatible with pwntools, but it is likely that we will be mostly
compatible.

.. code:: python

   from pcstools import *

   r = remote('exploitme.example.com', 31337)
   # EXPLOIT CODE GOES HERE
   r.send(asm(shellcraft.sh()))
   r.interactive()
'''

setup(
    name='pcstools',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',

    packages=find_packages(),
    version='0.3',
    data_files=[('',
                 glob.glob('*.md') + glob.glob('*.txt')),
                ],
    description="Tools for the course Proactive Computer Security at DIKU",
    long_description=long_description,
    author="Mathias Svensson",
    author_email="freaken@freaken.dk",
    url='https://github.com/DIKU-PCS/pcstools',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
