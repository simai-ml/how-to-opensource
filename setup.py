import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="QM How to Opensource by GMA",
    version="0.0.1",
    author="Grégoire Martinon, Vianney Taquet, Damien Hervault",
    author_email="gmartignon@quantmetry.com",
    description="A Quantmetry tutorial on how to publish an opensource python package.",
    license="BSD",
    keywords="example opensource tutorial",
    url="http://packages.python.org/how_to_opensource",
    packages=['how_to_opensource'],
    install_requires=["numpy>=1.20"],
    extras_require={
        "tests": ["flake8", "mypy", "pytest-cov"],
        "docs": ["sphinx", "sphinx-gallery", "sphinx_rtd_theme", "numpydoc"]
    },
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.9"
    ],
)
