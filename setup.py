from __future__ import with_statement
from setuptools import setup
import sys

# Do not update the version manually - it is managed by `bumpversion`.
version = '2.0.1rc'


REQUIRES = [
        'snowballstemmer',
        'six',
    ]


# Python3 to Python2 backport support.
if sys.version_info[0] == 2:
    REQUIRES.append('configparser == 3.5.0')


setup(
    name='pydocstyle',
    version=version,
    description="Python docstring style checker",
    long_description=open('README.rst').read(),
    license='MIT',
    author='Amir Rachum',
    author_email='amir@rachum.com',
    url='https://github.com/PyCQA/pydocstyle/',
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='pydocstyle, PEP 257, pep257, PEP 8, pep8, docstrings',
    packages=('pydocstyle',),
    package_dir={'': 'src'},
    package_data={'pydocstyle': ['data/*.txt']},
    install_requires=REQUIRES,
    entry_points={
        'console_scripts': [
            'pydocstyle = pydocstyle.cli:main',
        ],
    },
)
