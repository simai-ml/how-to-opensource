import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "QM How to Opensource",
    version = "0.0.1",
    author = "Grégoire Martignon, Vianney Taquet, Damien Hervault",
    author_email = "gmartignon@quantmetry.com",
    description = ("A Quantmetry tutorial on how to publish an opensource python package."),
    license = "BSD",
    keywords = "example opensource tutorial",
    url = "http://packages.python.org/how_to_opensource",
    packages=['how_to_opensource'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
