import setuptools

# Convert README.md to reStructuredText for PyPI
with open('README.md', 'r') as fd:
    long_description = fd.read()

setuptools.setup(
    name='pcstools',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',

    packages=setuptools.find_packages(),
    version='0.3',
    description="Tools for the course Proactive Computer Security at DIKU",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
